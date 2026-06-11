# Phase 08 - Itinerary Planning Agent

## Objective

Generate detailed travel itineraries.

---

## Agent Responsibilities

- Day-wise planning
- Time scheduling
- Activity allocation
- Travel optimization

---

## Agent Collaboration

Consumes:

- Research Agent Output
- Budget Agent Output
- Hotel Agent Output

---

## Workflow

Research Report

+

Budget Report

+

Hotel Report

↓

Groq Planning

↓

Itinerary

---

## Output

Day-wise travel plan.

---

## API Endpoint

```http
POST /itinerary
```