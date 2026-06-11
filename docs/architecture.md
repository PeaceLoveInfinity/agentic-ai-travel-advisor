# Autonomous AI Travel Advisor Architecture

## High-Level Architecture

User

↓

Frontend (Future React / Next.js)

↓

n8n Workflow Layer

↓

FastAPI Backend

↓

LangGraph Orchestration Layer

↓

Supervisor Agent

↓

Research Agent
Budget Agent
Hotel Agent
Itinerary Agent
Risk Agent

↓

External APIs

- Tavily Search
- OpenWeatherMap
- OpenStreetMap
- Foursquare Places API
- Serper API
- AviationStack

↓

Database

- SQLite (Development)
- PostgreSQL (Production)

---

## Technology Stack

### Frontend

Planned:

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion

---

### Backend

- FastAPI
- Python

---

### Agent Framework

- LangGraph
- CrewAI (Future Integration)

---

### LLM Layer

Current:

- Groq
- Llama 3.3 70B

Future:

- DeepSeek-R1
- Gemini
- OpenAI

---

### Databases

Development:

- SQLite

Production:

- PostgreSQL

---

### Observability

Planned:

- LangSmith
- Logging
- Agent Tracing

---

## Agent Architecture

### Research Agent

Tools:

- Tavily
- Search APIs

Purpose:

- Destination intelligence

---

### Budget Agent

Purpose:

- Travel cost estimation

---

### Hotel Agent

Tools:

- OpenStreetMap
- Location APIs

Purpose:

- Hotel recommendations

---

### Itinerary Agent

Purpose:

- Day-wise travel planning

---

### Risk Agent

Tools:

- OpenWeatherMap

Purpose:

- Travel advisory

---

### Supervisor Agent

Purpose:

- Agent orchestration
- Final recommendation generation

---

## LangGraph Workflow

START

↓

Research

↓

Budget

↓

Hotel

↓

Itinerary

↓

Risk

↓

Supervisor

↓

END

---

## Current Status

Completed:

- Environment Setup
- FastAPI APIs
- Database Layer
- Logging
- Research Agent
- Budget Agent
- Hotel Agent
- Itinerary Agent
- Risk Agent
- Supervisor Agent
- LangGraph Orchestration

Upcoming:

- Memory
- Checkpointing
- Human-in-the-loop
- n8n Enterprise Workflows
- React Frontend
- Docker
- CI/CD
- Production Deployment

## Memory Layer

Current:

- LangGraph MemorySaver
- Thread-Based Sessions

Capabilities:

- Workflow Checkpointing
- Session Isolation
- State Persistence (Runtime)

Planned:

- PostgreSQL Persistence
- Long-Term User Memory
- Conversation Recall

## Human-in-the-Loop Layer

Implemented:

- Approval Manager
- Approval Node
- Conditional Routing

Capabilities:

- User Validation
- Workflow Control
- Approval-Based Execution

Planned:

- LangGraph Interrupts
- React UI Approval
- n8n Approval Workflows
- Email Approval Links