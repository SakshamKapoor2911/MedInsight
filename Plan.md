# MedLama Implementation Plan

This document outlines a 15-day, phase-based plan to build the MedLama platform—a cloud-native, microservices-based system for AI-powered medical diagnostics. The plan is inspired by enterprise engineering practices and rapid AI-driven development, and is structured to reflect the modular architecture described in the README.

## Phase 1: Project Scaffolding & Infrastructure (Days 1-2)
- [ ] Initialize repository and folder structure for all microservices:
    - Go backend (`services/backend-service`): API gateway, Google Pub/Sub messaging, auth, DB ops
    - Python AI/ML service (`services/ai-service`): LangGraph agents, LLM integration, NIM orchestration
    - Angular frontend (`services/frontend`): UI, components, services, API integration
- [ ] Set up Python virtual environment, Go module, and Node.js workspace
- [ ] Add basic README, .gitignore, and requirements files for each service
- [ ] Create Docker configuration for local development (all services)
- [ ] Set up MongoDB (local or Atlas)
- [ ] Scaffold deployment directory for Docker Compose, Kubernetes manifests, NIM configuration, and CI/CD

## Phase 2: Core Backend & AI/ML Services (Days 3-5)
- [ ] Implement Go backend skeleton (API gateway, Google Pub/Sub messaging, authentication, DB ops)
- [ ] Implement Python AI/ML service skeleton (FastAPI/Flask, LangGraph for conversation state)
- [ ] Design NVIDIA NIM integration with Gemma 2 for self-hosted medical reasoning
- [ ] Add endpoints for user authentication, conversation, and research
- [ ] Connect both backend and AI/ML service to MongoDB for storing conversation history
- [ ] Integrate Perplexity API for medical literature research and evidence gathering
- [ ] Write unit tests for backend and AI/ML logic

## Phase 3: Frontend Development (Days 6-8)
- [ ] Scaffold Angular + TypeScript frontend using Angular CLI
- [ ] Implement authentication screens and chat UI with Angular components and services
- [ ] Connect frontend to backend API (REST/WebSocket)
- [ ] Add real-time updates for chat and notifications
- [ ] Style with modern, responsive design
- [ ] Write frontend unit tests (Karma/Jasmine)

## Phase 4: Real-time Features (Days 9-10)
- [ ] Implement WebSocket support for live chat and alerts (Go backend, Angular frontend)
- [ ] Integrate notification/alert system (backend, AI/ML, frontend)
- [ ] Write integration tests for real-time flows

## Phase 5: Testing & Quality Assurance (Days 11-12)
- [ ] Achieve >80% unit test coverage (Go backend, Python AI/ML, Angular frontend)
- [ ] Implement integration tests for critical user journeys (all services)
- [ ] Add end-to-end tests (Cypress or Protractor)
- [ ] Perform security and privacy review (data privacy, secure auth, encrypted storage)

## Phase 6: Cloud/Deployment & Monitoring (Days 13-14)
- [ ] Containerize all microservices (Go backend, Python AI/ML, Angular frontend) with Docker
- [ ] Set up Google Kubernetes Engine (GKE) cluster with GPU node pool for NVIDIA NIM
- [ ] Deploy NVIDIA NIM on GKE for self-hosted model inference
- [ ] Prepare Kubernetes manifests for all services deployment
- [ ] Set up Cloud Build for CI/CD pipeline and automated deployments
- [ ] Configure Google Cloud Operations for monitoring, logging, and alerting

## Phase 7: Documentation & Final Review (Day 15)
- [ ] Update README and API documentation (Swagger/OpenAPI)
- [ ] Add architecture diagrams and deployment instructions
- [ ] Document engineering decisions and patterns
- [ ] Conduct UI/UX and code quality review (Angular best practices)
- [ ] Final polish and project handoff

---

## 🚀 Immediate Implementation Action Items
*Priority order for transitioning from current monolithic structure to planned microservices architecture*

### Action Item 1: Create the Proper Folder Structure ⚡ **[START HERE]**
**Current State**: Monolithic Flask app with mixed concerns (app.py, llm.py, multiturn.py in root)
**Target State**: Clean microservices separation as documented in README
**Details**:
- Create `services/` directory with subdirectories for `backend-service/`, `ai-service/`, `frontend/`
- Create `deployment/` directory for Docker Compose, K8s manifests, NIM configs
- Create `scripts/` directory for utility scripts
- Preserve existing files temporarily while setting up new structure

### Action Item 2: Refactor Existing LLM Code into New AI/ML Service Structure
**Current State**: LangGraph implementation in `llm.py` and `multiturn.py` at project root
**Target State**: Organized Python AI/ML service in `services/ai-service/`
**Details**:
- Move and restructure LangGraph agents, conversation state management
- Organize as proper Python package: `/api` (FastAPI/Flask endpoints), `/agents` (LangGraph), `/models` (NIM integration), `/utils`
- Update imports and dependencies for new structure
- Integrate Gemma 2 via NVIDIA NIM for medical reasoning, keep Perplexity for research
- Update requirements.txt for the AI service

### Action Item 3: Set up Basic Go API Gateway
**Current State**: No Go backend exists
**Target State**: High-performance Go API gateway in `services/backend-service/`
**Details**:
- Create Go module structure with `/cmd` (main.go), `/internal` (api, pubsub, auth, db), `/pkg`
- Use lightweight framework (Gin or Echo) for REST/WebSocket handling
- Implement Google Pub/Sub messaging integration for AI service communication
- Add authentication and MongoDB database operations
- Create basic health check and API endpoints

### Action Item 4: Set up Basic Angular Frontend
**Current State**: Next.js/React components in `medLama/` directory
**Target State**: Modern Angular application in `services/frontend/`
**Details**:
- Initialize new Angular project using Angular CLI
- Migrate UI concepts from existing React components to Angular components
- Set up project structure: `/src/app/components`, `/services`, `/models`
- Implement authentication screens and chat UI with Angular best practices
- Connect to Go backend API via HTTP services and WebSocket integration

### Action Item 5: Create Docker and Kubernetes Configurations
**Current State**: No containerization or orchestration configs
**Target State**: Complete containerization and GKE deployment setup
**Details**:
- Create Dockerfiles for each service (Go backend, Python AI/ML, Angular frontend)
- Set up Docker Compose for local development environment
- Create Kubernetes manifests for GKE deployment in `deployment/` directory
- Configure NVIDIA NIM deployment with Gemma 2 model on GPU node pool
- Set up Cloud Build CI/CD pipeline configuration

---

## Development Approach
- Daily check-ins and progress tracking
- Test-driven development for critical components
- Focus on modular, scalable, and secure design
- Clear separation of Go backend, Python AI/ML, and frontend services for team scalability
- Containerization and cloud-native deployment



## Best Practices for Solo Development, Testing, and Integration

**Development Workflow**
- Use clear commit messages and maintain a logical commit history.
- Regularly push changes to a remote repository for backup and version control.
- Keep documentation (README, API docs, architecture notes) up to date as you build.

**Testing**
- Write unit tests for all critical logic in each microservice.
- Aim for high test coverage (>80%) to catch regressions early.
- Use automated test runners (e.g., `go test`, `pytest`, `jest`) before major commits.
- Mock external APIs/services in tests for reliability.

**Integration**
- Use Docker Compose to run all services locally for end-to-end testing.
- Regularly test integration points between backend, AI/ML, and frontend.
- Use a simple CI workflow (e.g., GitHub Actions) for automated builds and tests.
- Containerize all services for consistency between local and cloud environments.

**General Tips**
- Refactor code regularly to keep it clean and maintainable.
- Take notes on engineering decisions and architectural changes.
- Use AI tools for code review, suggestions, and troubleshooting.


*And most importantly, build with ❤️ to organize the world’s healthcare information, making it universally accessible and useful.*
