package api
import (
	"testing"
	"net/http"
	"net/http/httptest"
	"strings"
	"encoding/json"
)
func TestRegisterBadRequest(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("POST", "/api/auth/register", strings.NewReader("badjson"))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	if w.Code != http.StatusBadRequest {
		t.Errorf("Expected 400 for bad register, got %d", w.Code)
	}
}

func TestLoginBadRequest(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("POST", "/api/auth/login", strings.NewReader("badjson"))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	if w.Code != http.StatusBadRequest {
		t.Errorf("Expected 400 for bad login, got %d", w.Code)
	}
}

func TestLoginWrongPassword(t *testing.T) {
	r := SetupRouter()
	// Register user
	w := httptest.NewRecorder()
	registerBody := `{"username":"user2","password":"pass2"}`
	req, _ := http.NewRequest("POST", "/api/auth/register", strings.NewReader(registerBody))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	// Try wrong password
	w2 := httptest.NewRecorder()
	loginBody := `{"username":"user2","password":"wrong"}`
	req2, _ := http.NewRequest("POST", "/api/auth/login", strings.NewReader(loginBody))
	req2.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w2, req2)
	if w2.Code != http.StatusUnauthorized {
		t.Errorf("Expected 401 for wrong password, got %d", w2.Code)
	}
}

func TestAuthMiddlewareValidToken(t *testing.T) {
	r := SetupRouter()
	// Register and login
	w := httptest.NewRecorder()
	registerBody := `{"username":"user3","password":"pass3"}`
	req, _ := http.NewRequest("POST", "/api/auth/register", strings.NewReader(registerBody))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	w2 := httptest.NewRecorder()
	loginBody := `{"username":"user3","password":"pass3"}`
	req2, _ := http.NewRequest("POST", "/api/auth/login", strings.NewReader(loginBody))
	req2.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w2, req2)
	// Extract token
	var resp map[string]string
	json.Unmarshal(w2.Body.Bytes(), &resp)
	token := resp["access_token"]
	// Try accessing /ws with token
	w3 := httptest.NewRecorder()
	req3, _ := http.NewRequest("GET", "/ws", nil)
	req3.Header.Set("Authorization", "Bearer "+token)
	r.ServeHTTP(w3, req3)
	// Should not be unauthorized (upgrade will fail, but not 401)
	if w3.Code == http.StatusUnauthorized {
		t.Errorf("Expected upgrade error, not 401 for valid token, got %d", w3.Code)
	}
}


func TestHealthEndpoint(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/health", nil)
	r.ServeHTTP(w, req)
	if w.Code != http.StatusOK {
		t.Errorf("Expected status 200, got %d", w.Code)
	}
}

func TestRegisterAndLogin(t *testing.T) {
	r := SetupRouter()

	// Register user
	w := httptest.NewRecorder()
	registerBody := `{"username":"testuser","password":"testpass"}`
	req, _ := http.NewRequest("POST", "/api/auth/register", 
    strings.NewReader(registerBody))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	if w.Code != http.StatusOK {
		t.Errorf("Register failed: got %d", w.Code)
	}

	// Login user
	w2 := httptest.NewRecorder()
	loginBody := `{"username":"testuser","password":"testpass"}`
	req2, _ := http.NewRequest("POST", "/api/auth/login", 
    strings.NewReader(loginBody))
	req2.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w2, req2)
	if w2.Code != http.StatusOK {
		t.Errorf("Login failed: got %d", w2.Code)
	}
}

func TestLoginInvalidCredentials(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	loginBody := `{"username":"nouser","password":"badpass"}`
	req, _ := http.NewRequest("POST", "/api/auth/login", 
    strings.NewReader(loginBody))
	req.Header.Set("Content-Type", "application/json")
	r.ServeHTTP(w, req)
	if w.Code != http.StatusUnauthorized {
		t.Errorf("Expected 401 for invalid login, got %d", w.Code)
	}
}

func TestAuthMiddlewareUnauthorized(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/ws", nil)
	r.ServeHTTP(w, req)
	if w.Code != http.StatusUnauthorized {
		t.Errorf("Expected 401 for missing token, got %d", w.Code)
	}
}

// WebSocketHandler is best tested with integration tests, but we can check upgrade failure
func TestWebSocketHandlerUpgradeFailure(t *testing.T) {
	r := SetupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/ws", nil)
	req.Header.Set("Authorization", "Bearer invalidtoken")
	r.ServeHTTP(w, req)
	if w.Code != http.StatusUnauthorized {
		t.Errorf("Expected 401 for invalid token, got %d", w.Code)
	}
}
