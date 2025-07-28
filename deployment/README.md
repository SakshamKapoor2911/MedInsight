# Deployment Configuration

## Purpose
This directory contains all deployment-related configurations for the MedLama platform:
- Docker configurations for containerization
- Kubernetes manifests for GKE deployment
- NVIDIA NIM deployment configurations
- CI/CD pipeline definitions

## Structure
```
deployment/
├── docker/                # Docker configurations
│   ├── docker-compose.yml # Local development environment
│   ├── backend.Dockerfile # Go backend service
│   ├── ai-service.Dockerfile # Python AI/ML service
│   └── frontend.Dockerfile # Angular frontend service
├── kubernetes/           # Kubernetes manifests
│   ├── namespace.yaml   # Kubernetes namespace
│   ├── backend/         # Backend service K8s configs
│   ├── ai-service/      # AI service K8s configs
│   ├── frontend/        # Frontend service K8s configs
│   └── monitoring/      # Monitoring and logging configs
├── nvidia-nim/          # NVIDIA NIM deployment
│   ├── nim-deployment.yaml # NIM pod deployment
│   ├── nim-service.yaml    # NIM service configuration
│   └── gpu-nodepool.yaml  # GPU node pool configuration
├── ci-cd/               # CI/CD pipeline configurations
│   ├── cloudbuild.yaml # Google Cloud Build configuration
│   └── github-actions/ # GitHub Actions workflows
└── README.md          # This file
```

## Technology Stack
- **Containerization**: Docker with multi-stage builds
- **Orchestration**: Google Kubernetes Engine (GKE)
- **AI Inference**: NVIDIA NIM on GPU-enabled nodes
- **CI/CD**: Google Cloud Build + GitHub Actions
- **Monitoring**: Google Cloud Operations Suite

## Environment Management
- **Local Development**: Docker Compose for all services
- **Staging**: GKE cluster with basic configurations
- **Production**: GKE cluster with GPU node pool, monitoring, and scaling

## Next Steps
1. Create Docker Compose for local development
2. Build Dockerfiles for each service
3. Set up GKE cluster with GPU node pool
4. Configure NVIDIA NIM deployment
5. Set up Cloud Build CI/CD pipeline
