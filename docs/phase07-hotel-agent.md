# Phase 07 - Hotel Recommendation Agent

## Objective

Recommend suitable hotels based on destination and budget.

---

## Agent Responsibilities

- Hotel discovery
- Hotel ranking
- Hotel recommendations

---

## Tools Used

### OpenStreetMap (Nominatim)

Purpose:

Location intelligence.

---

## Workflow

Destination

↓

Location Search

↓

Groq Analysis

↓

Hotel Recommendations

---

## Output

- Budget Hotel
- Best Value Hotel
- Premium Hotel

---

## API Endpoint

```http
POST /hotels
```