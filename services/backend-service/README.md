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
- **Framework**: Gin or Echo (lightweight HTTP framework)
- **Messaging**: Google Cloud Pub/Sub
- **Database**: MongoDB with official Go driver
- **Authentication**: JWT tokens
- **WebSockets**: Gorilla WebSocket or similar

## Next Steps
1. Initialize Go module (`go mod init`)
2. Set up basic HTTP server with health check endpoint
3. Implement Pub/Sub publisher for AI service communication
4. Add MongoDB connection and basic CRUD operations
5. Implement authentication middleware
