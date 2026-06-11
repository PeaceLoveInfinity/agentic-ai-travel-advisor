# Phase 02 - Environment Setup

## Objective

Prepare the project development environment and foundational structure.

---

## Folder Structure

Created:

- agents/
- graph/
- tools/
- api/
- frontend/
- db/
- config/
- tests/
- docs/
- logs/

---

## Python Environment

Virtual Environment:

```bash
python -m venv venv
```

Activation:

```bash
venv\Scripts\activate
```

---

## Installed Packages

- FastAPI
- LangGraph
- LangChain
- Streamlit
- SQLAlchemy
- Requests
- Python-Dotenv

---

## API Keys Configured

- Groq API
- Tavily API
- Serper API
- OpenWeatherMap API

---

## Initial Backend

FastAPI Health Endpoint:

```http
GET /
```

Response:

```json
{
  "status":"running"
}
```

---

## Initial Frontend

Basic Streamlit application created for testing.