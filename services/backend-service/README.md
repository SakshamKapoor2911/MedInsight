# Backend Service (Go)

## Purpose
High-performance Go API gateway that handles:
- REST/WebSocket API endpoints
- Google Pub/Sub messaging integration
- User authentication and authorization
- MongoDB database operations
- Request routing and load balancing

## Structure
```
backend-service/
├── cmd/                    # Application entrypoints
│   └── main.go            # Main application entry
├── internal/              # Private application code
│   ├── api/               # HTTP handlers and routes
│   ├── pubsub/            # Google Pub/Sub integration
│   ├── auth/              # Authentication logic
│   └── db/                # Database operations
├── pkg/                   # Public library code
├── go.mod                 # Go module definition
├── go.sum                 # Go module checksums
└── README.md             # This file
```

## Technology Stack

## Next Steps
1. Initialize Go module (`go mod init`)
2. Set up basic HTTP server with health check endpoint
3. Implement Pub/Sub publisher for AI service communication
4. Add MongoDB connection and basic CRUD operations
5. Implement authentication middleware
## Technology Stack
 - **Framework**: Gin or Echo (lightweight HTTP framework)
 - **Database**: MongoDB with official Go driver
 - **Authentication**: JWT tokens
 - **WebSockets**: Gorilla WebSocket or similar

## Local Development & Testing

This service is designed for local use only. All cloud/deployment plans are deferred.

### Setup
1. Initialize Go module (if not already):
	```bash
	go mod tidy
	```
2. Start MongoDB locally (or use Docker Compose).
3. Run the backend server:
	```bash
	go run ./cmd/main.go
	```

### Running Tests
Run all unit and integration tests locally:
```bash
go test ./...
```

### Notes
- All authentication, messaging, and DB logic is implemented for local development and testing only.
- See code comments for details on each module and handler.
