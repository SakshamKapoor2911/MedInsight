# MedLama: A Scalable, AI-Powered Medical Diagnostics Platform

<p align="center">
  </p>

## 🚀 Project Vision

**MedLama** is an advanced, AI-powered platform designed to simulate preliminary medical diagnostic consultations. Originally a full-stack application, the project is currently being re-architected into a **resilient, distributed system** capable of handling high-concurrency workloads.

The core of the system is a sophisticated AI agent, built with **LangGraph**, that achieved **92% diagnostic accuracy** against a medical expert's evaluation. This agent is being transitioned to run on a scalable microservices backend powered by **Go** and orchestrated by **Kubernetes**.

---

## 📋 Table of Contents
* [Key Features](#-key-features)
* [System Architecture](#️-system-architecture)
* [Project Roadmap](#-project-roadmap)
* [Tech Stack](#️-tech-stack)
* [Local Setup](#️-local-setup)

---

## ✨ Key Features

* **Scalable Backend Architecture:** The system is built on a **microservices architecture** using **Go**, designed for high availability and horizontal scaling.
* **Fault-Tolerant Communication:** A custom message queue built with **Go** and the **Raft consensus algorithm** ensures asynchronous, reliable communication between services.
* **Stateful Agentic Workflow:** The core AI agent, engineered with **LangGraph**, manages a robust, multi-step conversational workflow.
* **Autonomous Tool Use:** The agent intelligently determines when to invoke external research tools (**Perplexity API**) to deepen its analysis.
* **Full-Stack Implementation:** A complete application featuring a modern frontend built with **Next.js** and **TypeScript**.

## 🏗️ System Architecture

The new architecture is designed for scalability and resilience. For a detailed breakdown of the services and design patterns used, please see the [**System Architecture Documentation**](./ARCHITECTURE.md).

## 🗺️ Project Roadmap

This project is being developed in planned phases to ensure a robust and well-engineered final product.

* **Phase 1: Distributed Message Queue Core (In Progress)**
    * [ ] Build the core message queue in Go with a gRPC API.
    * [ ] Integrate the Raft consensus algorithm via `hashicorp/raft`.
    * [ ] Containerize the service with Docker.
    * **Goal:** Create the fault-tolerant, distributed backbone for the entire system.

* **Phase 2: AI Agent Integration (Planned Q3 2025)**
    * [ ] Adapt the existing Python AI agents to communicate via the message queue.
    * [ ] Implement producer/consumer logic for asynchronous task handling.
    * **Goal:** Decouple the AI logic into independent, scalable microservices.

* **Phase 3: Kubernetes Deployment (Planned Q4 2025)**
    * [ ] Write Kubernetes manifests for all services.
    * [ ] Deploy the full application to a cloud-based Kubernetes cluster.
    * [ ] Connect the existing Next.js frontend to the new backend.
    * **Goal:** Demonstrate operational readiness and automated orchestration.

---
