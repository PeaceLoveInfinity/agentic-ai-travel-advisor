# Phase 13 - Human-in-the-Loop (HITL)

## Overview

Phase 13 introduces human approval into the travel planning workflow.

Instead of immediately completing execution after generating a travel package, the system now pauses and requests user approval.

---

## Objectives

- Add human oversight
- Prevent fully autonomous execution
- Enable user validation
- Support workflow resubmission

---

## Workflow

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

Approval Node

↓

User Decision

↓

Approve?

├── Yes → END

└── No → Regenerate

---

## Components

### Approval Manager

Responsibilities:

- Capture user decision
- Validate input

---

### Approval Node

Responsibilities:

- Pause workflow
- Request approval
- Store decision

---

### Conditional Routing

LangGraph conditional edges determine:

- Approved path
- Rejected path

---

## State Updates

Added:

```python
approval_status
```

to TravelState.

---

## Benefits

- Human oversight
- Safer AI workflows
- Better decision quality
- Enterprise readiness

---

## Future Enhancements

- Web-based approvals
- Email approvals
- Slack approvals
- n8n approval workflows
- Multi-level approvals