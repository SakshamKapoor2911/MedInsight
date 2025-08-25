package main

import (
	"fmt"
	"net/http"
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool { return true },
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "OK")
}

func wsHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println("WebSocket upgrade error:", err)
		return
	}
	defer conn.Close()
	for {
		_, msg, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("WebSocket read error:", err)
			break
		}
		fmt.Printf("Received: %s\n", msg)
		if err := conn.WriteMessage(websocket.TextMessage, msg); err != nil {
			fmt.Println("WebSocket write error:", err)
			break
		}
	}
}

func main() {
	http.HandleFunc("/health", healthCheck)
	http.HandleFunc("/ws", wsHandler)
	fmt.Println("Server started on :8080")
	http.ListenAndServe(":8080", nil)
}
