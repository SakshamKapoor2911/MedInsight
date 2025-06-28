# MedLama: AI-Powered Medical Diagnostics Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangGraph-black?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph">
  <img src="https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini">
</p>

## 🚀 Project Overview

**MedLama** is a full-stack web application featuring an intelligent AI agent that simulates a preliminary medical diagnostic consultation. The agent engages in a multi-turn conversation with the user to gather symptoms, autonomously decides when to conduct external research, and synthesizes its findings into a structured diagnostic report.

This project demonstrates an advanced, stateful agentic workflow. The core AI logic is built with **LangGraph**, enabling the agent to reason about the conversation, manage its internal state, and decide which tools to use, such as calling the **Perplexity API** for up-to-date medical information. The backend is powered by Python, and the user interface is a modern, responsive web app built with **Next.js** and **TypeScript**.

---

## 📋 Table of Contents
* [Key Features](#-key-features)
* [System Architecture](#️-system-architecture)
* [Tech Stack](#️-tech-stack)
* [Local Setup](#️-local-setup)
* [The AI Agent's Core Logic](#-the-ai-agents-core-logic)
* [Future Work](#-future-work)

---

## ✨ Key Features

* **Stateful Agentic Workflow:** Engineered with **LangGraph** to create a robust, multi-step agent that manages conversational state, making it resilient and predictable.
* **Autonomous Tool Use:** The agent intelligently determines when it has gathered enough information from the user versus when it needs to invoke external research tools (Perplexity API) to deepen its analysis.
* **Full-Stack Implementation:** A complete application featuring a modern frontend built with **Next.js, TypeScript, and Tailwind CSS**, and a powerful **Python** backend serving the AI logic.
* **Interactive Chat Interface:** A clean, user-friendly UI (built with Shadcn UI) for seamless interaction with the diagnostic agent.
* **Structured Medical Reporting:** The agent concludes the consultation by generating a detailed, easy-to-read diagnostic report in Markdown format, complete with differential diagnoses and confidence scores.

## 🏗️ System Architecture

The application is architected with a decoupled frontend and backend. The user interacts with the Next.js application, which communicates with the Python backend via an API. The backend orchestrates the LangGraph agent to manage the diagnostic process.

```plaintext
+---------------------+      +-----------------+      +-----------------------+      +-------------------+
|   Next.js Frontend  |<---->|  Python Backend |<---->|    LangGraph Agent    |<---->|  External Tools   |
| (TypeScript, React) |      | (API Server)    |      | (Stateful Workflow)   |      | (Gemini, Perplexity)|
+---------------------+      +-----------------+      +-----------------------+      +-------------------+

Frontend: The user enters their symptoms into the chat interface.

Backend API: The Next.js app sends the user's message to the Python server.

LangGraph Agent: The backend invokes the LangGraph agent, which manages the state of the conversation.

Conversation Node: The agent first uses Google Gemini to ask clarifying questions.

Router: Based on the conversation, a conditional edge decides whether to continue the conversation or proceed to research.

Research Node: If research is needed, the agent calls the Perplexity API tool with a focused query.

Analysis Node: The research findings are synthesized into a final report.

Response: The final report or the next question is streamed back through the API to the frontend.
```
## 🛠️ Tech Stack

Technologies Used

Frontend
```
Next.js, React, TypeScript, Tailwind CSS, Shadcn UI
```
Backend
```
Python, LangGraph, LangChain, Google Gemini, Perplexity API
```
Database
```
MongoDB (for conversation history and user data)
```
⚙️ Local Setup
To run this project locally, you will need to set up both the backend and the frontend.

Prerequisites  
```
Node.js and npm

Python 3.10+ and pip

GEMINI_API_KEY from Google AI Studio

PERPLEXITY_API_KEY from Perplexity AI
```
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
```
Frontend Setup
Navigate to the frontend directory:
```
cd medLama
```
Install npm dependencies:
```
npm install
```
Run the frontend development server:
```
npm run dev
```
Open your browser and navigate to http://localhost:3000 to see the application running.

🧠 The AI Agent's Core Logic
The intelligence of this application lies in the stateful graph constructed with LangGraph. Unlike a simple LLM chain, this graph can loop, make decisions, and manage a multi-turn conversation effectively.

For a deeper, code-level understanding of how the agent was designed and built, you can explore the original proof-of-concept in the Jupyter Notebook here.

🔮 Future Work
Database Integration: Fully integrate MongoDB to store and retrieve conversation history for returning users.

User Authentication: Implement a secure authentication system to manage user profiles and protect their data.

Enhanced Tools: Add more specialized tools to the agent, such as a medical knowledge base lookup or a drug interaction checker.

Deployment: Containerize the application with Docker and deploy it to a cloud service like Vercel (for frontend) and a PaaS (for backend).
