# MedLama: A Scalable, AI-Powered Medical Diagnostics Platform

<p align="center">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/LangGraph-black?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
</p>

## 🚀 Project Vision

**MedLama** is an advanced AI platform designed to conduct preliminary medical diagnostic consultations. The core of this platform is a sophisticated agent, built with **LangGraph** and **Gemini**, which has **achieved 92% diagnostic accuracy** against a medical expert's evaluation of a complex disease case.

The project is currently undergoing a significant architectural evolution, migrating from a monolithic Python application to a **resilient, distributed system** built with **Go** and orchestrated by **Kubernetes**. This will ensure high availability, fault tolerance, and the ability to scale to handle high-concurrency workloads.

---

## 📋 Table of Contents
* [Key Features](#-key-features)
* [Target Architecture](#️-target-architecture)
* [Project Roadmap](#-project-roadmap)
* [Technology Stack](#️-technology-stack)
* [Running the Prototype](#-running-the-prototype)

---

## ✨ Key Features

* **Proven Diagnostic Accuracy:** The core AI agent has been benchmarked at **92% accuracy** against a medical expert.
* **Scalable Backend Architecture:** The new system is being built on a **microservices architecture** using **Go** for high performance and low-latency communication.
* **Fault-Tolerant by Design:** The system's backbone is a high-throughput message queue leveraging the **Raft consensus algorithm** for data replication and cluster resilience.
* **Advanced Agentic Workflow:** The AI agent uses **LangGraph** to manage a robust, multi-step conversational state, allowing it to reason and autonomously use tools.
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
