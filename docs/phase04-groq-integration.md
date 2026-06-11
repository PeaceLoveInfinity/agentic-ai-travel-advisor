# Phase 04 - Groq LLM Integration

## Objective

Integrate Groq-hosted LLMs as the reasoning engine.

---

## Components Created

### LLM Layer

Files:

- groq_client.py
- model_factory.py

---

## Supported Models

Current:

- Llama 3.3 70B

Future:

- DeepSeek-R1
- Gemini
- OpenAI

---

## AI Service Layer

Created:

```text
services/travel_ai.py
```

Responsibilities:

- Prompt execution
- Response generation

---

## API Endpoint

```http
POST /ask
```

Purpose:

General AI travel interaction.

---

## Benefits

- Model abstraction
- Centralized LLM access
- Future model switching