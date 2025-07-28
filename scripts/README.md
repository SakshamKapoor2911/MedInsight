# Scripts Directory

## Purpose
This directory contains utility scripts for development, deployment, and maintenance tasks.

## Scripts (To be created)
```
scripts/
├── setup/
│   ├── setup-dev-env.sh     # Set up local development environment
│   ├── setup-gke-cluster.sh # Create GKE cluster with GPU nodes
│   └── setup-nim.sh         # Deploy NVIDIA NIM on GKE
├── build/
│   ├── build-all.sh         # Build all services
│   ├── build-backend.sh     # Build Go backend
│   ├── build-ai-service.sh  # Build Python AI service
│   └── build-frontend.sh    # Build Angular frontend
├── deploy/
│   ├── deploy-local.sh      # Deploy to local Docker Compose
│   ├── deploy-staging.sh    # Deploy to staging GKE
│   └── deploy-prod.sh       # Deploy to production GKE
├── test/
│   ├── run-tests.sh         # Run all tests
│   ├── integration-test.sh  # Run integration tests
│   └── e2e-test.sh         # Run end-to-end tests
└── utils/
    ├── logs.sh             # Fetch logs from services
    ├── cleanup.sh          # Clean up resources
    └── health-check.sh     # Check service health
```

## Usage
Each script will be executable and include proper documentation and error handling.

## Next Steps
1. Create development environment setup script
2. Add build automation scripts
3. Create deployment scripts for each environment
4. Add testing and utility scripts
