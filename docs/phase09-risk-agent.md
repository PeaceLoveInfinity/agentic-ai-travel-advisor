# Phase 09 - Risk Advisory Agent

## Objective

Assess travel risks and advisories.

---

## Agent Responsibilities

- Weather analysis
- Safety assessment
- Travel advisory generation

---

## Tools Used

### OpenWeatherMap

Provides:

- Temperature
- Conditions
- Wind
- Humidity

---

## Workflow

Weather Data

↓

Groq Risk Analysis

↓

Risk Report

---

## Output

- Risk Level
- Travel Advisory
- Recommended Precautions

---

## API Endpoint

```http
POST /risk
```