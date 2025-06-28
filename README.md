# MedLama: A Scalable, AI-Powered Medical Diagnostics Platform

## 🚀 Project Vision

**MedLama** is an advanced, AI-powered platform designed to simulate preliminary medical diagnostic consultations. Originally a full-stack application, the project is currently being re-architected into a **resilient, distributed system** capable of handling high-concurrency workloads.

The core of the system is a sophisticated AI agent, built with **LangGraph**, that achieved **92% diagnostic accuracy** against a medical expert's evaluation. This agent is being transitioned to run on a scalable microservices backend powered by **Go** and orchestrated by **Kubernetes**.

---

## 📋 Table of Contents
* [Key Features](#-key-features)
* [Target Architecture](#️-target-architecture)
* [Project Roadmap](#-project-roadmap)
* [Technology Stack](#️-technology-stack)
* [Running the Prototype](#-running-the-prototype)

---

## ✨ Key Features

* **Proven Diagnostic Accuracy:** The core AI agent has been benchmarked at **92% accuracy** against a medical expert on a complex disease case.
* **Scalable Backend Architecture:** The system is built on a **microservices architecture** using **Go** for high-performance, low-latency communication.
* **Fault-Tolerant by Design:** The system's backbone is a high-throughput message queue leveraging the **Raft consensus algorithm** for data replication and cluster resilience.
* **Advanced Agentic Workflow:** The AI agent uses **LangGraph** to manage a robust, multi-step conversational state, allowing it to reason and autonomously use external tools.
* **Modern Frontend:** A responsive and interactive user interface built with **Next.js** and **TypeScript**.

## 🏗️ Target Architecture

The new architecture is designed for scalability and resilience. The monolithic backend is being decomposed into a set of independent, communicating microservices.

```plaintext
+---------------------+   +-----------------+   +-------------------------+   +----------------------+
|                     |   |                 |   |                         |   |                      |
|  Next.js Frontend   |-->|  API Gateway    |-->|  Distributed Message    |-->|  AI Agent Services   |
| (React, TypeScript) |   |      (Go)       |   |   Queue (Go & Raft)     |   | (Python, LangGraph)  |
|                     |   |                 |   |                         |   |                      |
+---------------------+   +-----------------+   +-------------------------+   +----------------------+
API Gateway (Go): A single, high-performance entry point for all client traffic, responsible for routing, authentication, and rate limiting.

Distributed Message Queue (Go & Raft): The asynchronous backbone of the system, ensuring reliable, fault-tolerant communication between services.

AI Agent Services (Python): The core agent logic, broken into smaller microservices that can be scaled independently (e.g., Intake, Research, Synthesis).
```
## 🗺️ Project Roadmap
This project is being developed in planned phases. The source code for the new Go-based services will be hosted in a separate repository upon completion of Phase 1.

Phase 1: Distributed Message Queue Core (In Progress - Est. Q3 2025)

[ ] Build the core message queue in Go with a gRPC API.

[ ] Integrate the Raft consensus algorithm via hashicorp/raft.

[ ] Containerize the service with Docker.

Goal: Create the fault-tolerant, distributed backbone for the system.

Phase 2: AI Agent Integration (Planned Q4 2025)

[ ] Adapt the existing Python AI agents to communicate via the message queue.

[ ] Implement producer/consumer logic for asynchronous task handling.

Goal: Decouple the AI logic into independent, scalable microservices.

Phase 3: Kubernetes Deployment (Planned Q1 2026)

[ ] Write Kubernetes manifests for all services.

[ ] Deploy the full application to a cloud-based Kubernetes cluster.

Goal: Demonstrate operational readiness and automated orchestration.

## 🛠️ Technology Stack
Backend Systems & Architecture
Go, Docker, Kubernetes, Raft Consensus Algorithm, gRPC
AI & Application Logic
Python, LangGraph, LangChain, Google Gemini, Perplexity API
Frontend & Database
Next.js, React, TypeScript, Tailwind CSS, MongoDB
⚙️ Running the Prototype
The original, monolithic version of MedLama (which includes the 92% accurate AI agent) can be run locally.

Prerequisites
Node.js and npm

Python 3.10+ and pip

GEMINI_API_KEY from Google AI Studio

PERPLEXITY_API_KEY from Perplexity AI

Backend Setup
Clone the repository:


```
git clone [https://github.com/SakshamKapoor2911/Full_stack_Medical_Diagnostics.git](https://github.com/SakshamKapoor2911/Full_stack_Medical_Diagnostics.git)
cd Full_stack_Medical_Diagnostics
```
Set up a Python virtual environment:


```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Install Python dependencies:


```
pip install -r requirements.txt
```
Set up environment variables: Create a .env file in the root directory and add your API keys:
```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
PERPLEXITY_API_KEY="YOUR_PERPLEXITY_API_KEY"
```
Run the backend server: (Assuming your entry point is app.py)


```
python app.py
Frontend Setup
Navigate to the frontend directory:
```

```
cd medLama
Install npm dependencies:
```

```
npm install
Run the frontend development server:
```


npm run dev
Open your browser and navigate to http://localhost:3000 to see the application running.
