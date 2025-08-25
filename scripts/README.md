# Scripts Directory


## Purpose
This directory contains utility scripts for local development and maintenance tasks.

## Scripts (To be created)
```
scripts/
├── setup/
│   ├── setup-dev-env.sh     # Set up local development environment
├── build/
│   ├── build-all.sh         # Build all services
│   ├── build-backend.sh     # Build Go backend
│   ├── build-ai-service.sh  # Build Python AI service
│   └── build-frontend.sh    # Build frontend
├── deploy/
│   ├── deploy-local.sh      # Deploy to local Docker Compose
├── test/
│   ├── run-tests.sh         # Run all tests
│   ├── integration-test.sh  # Run integration tests
│   └── e2e-test.sh         # Run end-to-end tests
└── utils/
    ├── logs.sh             # Fetch logs from services
    ├── cleanup.sh          # Clean up resources
    └── health-check.sh     # Check service health
```

## Local Development & Testing
All scripts are intended for local development and testing only. Cloud/deployment scripts are deferred.

## Usage
Each script will be executable and include proper documentation and error handling.

## Next Steps
1. Create development environment setup script for local use
2. Add build automation scripts for local builds
3. Add testing and utility scripts for local workflows
