# Phase 14 – n8n Workflow Integration

## Objective

Integrate n8n with FastAPI and LangGraph to orchestrate the AI Travel Advisor workflow.

---

## Workflow Architecture

Webhook
↓
HTTP Request
↓
FastAPI
↓
LangGraph
↓
Multi-Agent Workflow
↓
Travel Package
↓
Respond to Webhook

---

## Nodes Implemented

### 1. Webhook Node

Purpose:
Receive travel planning requests.

Endpoint:

POST /webhook-test/travel-request

Sample Payload:

{
  "destination": "Goa",
  "budget": 50000,
  "duration": 5
}

---

### 2. HTTP Request Node

Purpose:
Forward request to FastAPI.

URL:

http://host.docker.internal:8000/graph-travel

Method:

POST

Body:

{
  "destination": "Goa",
  "budget": 50000,
  "duration": 5
}

---

### 3. LangGraph Invocation

FastAPI invokes LangGraph workflow.

Agents Executed:

- Research Agent
- Budget Agent
- Hotel Agent
- Itinerary Agent
- Risk Agent
- Supervisor Agent

---

### 4. Human Approval

Approval Node requests user confirmation.

Approve Travel Plan? (yes/no)

---

### 5. Travel Package Generation

Final recommendation package generated and returned to n8n.

---

## Key Learning Outcomes

- n8n workflow orchestration
- Webhook integration
- FastAPI integration
- LangGraph orchestration
- Human-in-the-loop workflows
- Docker networking using host.docker.internal
- Multi-agent workflow execution

---

## Result

Successfully executed:

Webhook
↓
n8n
↓
FastAPI
↓
LangGraph
↓
Groq
↓
Travel Package

with real-time AI-generated travel recommendations.