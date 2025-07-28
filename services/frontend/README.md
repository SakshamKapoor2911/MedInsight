# Frontend Service (Angular)

## Purpose
Modern Angular frontend application that provides:
- User authentication and authorization UI
- Real-time chat interface for medical consultations
- Responsive design for mobile and desktop
- Integration with Go backend API
- Medical conversation history and management

## Structure
```
frontend/
├── src/
│   ├── app/
│   │   ├── components/     # Reusable UI components
│   │   │   ├── auth/      # Authentication components
│   │   │   ├── chat/      # Chat interface components
│   │   │   └── shared/    # Shared components
│   │   ├── services/      # API and data services
│   │   │   ├── auth.service.ts
│   │   │   ├── chat.service.ts
│   │   │   └── api.service.ts
│   │   ├── models/        # TypeScript interfaces/models
│   │   │   ├── user.model.ts
│   │   │   └── conversation.model.ts
│   │   ├── guards/        # Route guards
│   │   └── interceptors/  # HTTP interceptors
│   ├── assets/           # Static assets
│   └── environments/     # Environment configurations
├── angular.json         # Angular CLI configuration
├── package.json        # Node.js dependencies
├── tsconfig.json       # TypeScript configuration
└── README.md          # This file
```

## Technology Stack
- **Framework**: Angular 17+ with TypeScript
- **UI Library**: Angular Material or PrimeNG
- **State Management**: RxJS for reactive programming
- **HTTP Client**: Angular HttpClient with WebSocket support
- **Styling**: Tailwind CSS or Angular Material theming
- **Testing**: Jasmine/Karma for unit tests, Cypress for E2E

## Current Implementation
The existing `medLama/` directory contains:
- Next.js/React components that need migration
- UI concepts and design patterns
- Component structure that can inform Angular implementation

## Next Steps
1. Initialize new Angular project using Angular CLI
2. Set up project structure and dependencies
3. Create authentication components and services
4. Build chat interface with real-time WebSocket integration
5. Connect to Go backend API endpoints
