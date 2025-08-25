
package api

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

// SetupRouter configures all HTTP routes for the backend service.
// This is for local development only; endpoints are not exposed to the cloud.
func SetupRouter() *gin.Engine {
	r := gin.Default()

	// Health check endpoint for local status monitoring
	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok"})
	})

	// User registration and login endpoints
	r.POST("/api/auth/register", Register)
	r.POST("/api/auth/login", Login)

	// WebSocket endpoint for real-time chat (local only)
	r.GET("/ws", AuthMiddleware(), WebSocketHandler)

	// TODO: Add real endpoints for chat, pubsub, auth, etc.

	return r
}
