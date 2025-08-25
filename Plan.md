# MedLama Implementation Plan

This document outlines a 15-day, phase-based plan to build the MedLama platform—a cloud-native, microservices-based system for AI-powered medical diagnostics. The plan is inspired by enterprise engineering practices and rapid AI-driven development, and is structured to reflect the modular architecture described in the README.

## Local Development & Zero-Cost Testing
- [ ] All services can be run and tested locally using Docker Compose
- [ ] Use local emulators/mocks for cloud dependencies (Google Pub/Sub Emulator, MongoDB local, NVIDIA NIM mock/CPU mode, etc.)
- [ ] All tests (unit, integration, E2E) pass locally before cloud deployment

## Phase 1: Project Scaffolding & Infrastructure (Days 1-2)
- [x] Go backend (`services/backend-service`): API gateway, Google Pub/Sub messaging, DB ops
- [x] Angular frontend (`services/frontend`): UI, components, services, API integration
- [x] Python AI/ML service (`services/ai-service`): LangGraph agents, LLM integration, NIM orchestration
- [x] Local development: All services run together via Docker Compose
- [x] Local MongoDB instance for dev/testing
- [x] Local Pub/Sub emulator for messaging
- [x] AI/ML service can run in CPU/mock mode locally
- [x] **Local Test Gate:** All health checks and basic unit tests pass locally

## Phase 2: Core Backend & AI/ML Services (Days 3-5)
- [ ] Write unit tests for backend and AI/ML logic (covering all endpoints, message flows, and DB ops)
- [ ] For AI/ML: Add basic accuracy and performance tests (e.g., ensure LLM returns medically plausible answers for sample prompts)
- [ ] Local integration: Backend and AI/ML communicate via local Pub/Sub emulator
- [ ] All endpoints and flows tested locally with Docker Compose
- [ ] **Local Test Gate:** All unit/integration/accuracy tests pass locally before cloud deployment

## Phase 3: Frontend Development (Days 6-8)
- [ ] Write frontend unit tests (Karma/Jasmine) for all components and services
- [ ] Validate UI against sample medical chat flows to ensure correct rendering and state
- [ ] Local integration: Frontend connects to backend via Docker Compose
- [ ] Real-time updates tested locally
- [ ] **Local Test Gate:** All frontend tests and flows validated locally

## Phase 4: Real-time Features (Days 9-10)
- [ ] Real-time chat and notifications tested with local Docker Compose setup
- [ ] Use local emulators/mocks for all messaging and notification flows
- [ ] **Local Test Gate:** Real-time features validated locally before cloud deployment

## Phase 5: Authentication & Security (Days 11-12)
- [ ] Implement user authentication (Go backend, Angular frontend)
- [ ] Add secure auth screens and backend logic
- [ ] Enforce encrypted storage for sensitive data
- [ ] Local authentication and security flows tested with Docker Compose
- [ ] **Local Test Gate:** Auth and security features validated locally before cloud deployment

## Phase 6: Cloud/Deployment & Monitoring (Days 13-14)
- [ ] Containerize all microservices (Go backend, Python AI/ML, Angular frontend) with Docker
- [ ] Set up Google Kubernetes Engine (GKE) cluster with GPU node pool for NVIDIA NIM
- [ ] Deploy NVIDIA NIM on GKE for self-hosted model inference
- [ ] Prepare Kubernetes manifests for all services deployment
- [ ] Set up Cloud Build for CI/CD pipeline and automated deployments
- [ ] Configure Google Cloud Operations for monitoring, logging, and alerting
- [ ] **Local Test Gate:** All services must be deployable and observable locally before cloud deployment

## Phase 7: Documentation & Final Review (Day 15)
- [ ] Update README and API documentation (Swagger/OpenAPI)
- [ ] Add architecture diagrams and deployment instructions
- [ ] Document engineering decisions and patterns
- [ ] Conduct UI/UX and code quality review (Angular best practices)
- [ ] Final polish and project handoff
- [ ] **Local Test Gate:** Documentation and final tests validated locally before cloud deployment

---
## Success Criteria: MVP & Demo Acceptance

- [ ] User can chat with the AI agent via the frontend and receive real-time responses (locally and in cloud)
- [ ] Conversation history is stored and retrievable from MongoDB (local and cloud)
- [ ] AI/ML service provides medically plausible answers and passes accuracy checks (locally and in cloud)
- [ ] Real-time notifications and alerts are delivered reliably (locally and in cloud)
- [ ] All core services (Go backend, Python AI/ML, Angular frontend) are containerized and run together locally (Docker Compose) and on GKE
- [ ] All test gates for Phases 1-4 are passed (unit, integration, performance, accuracy) locally before cloud deployment
- [ ] Demo is ready for review by Google Health or stakeholders

---
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
