# Phase 13 - Human-in-the-Loop (HITL)

## Overview

Phase 13 introduces Human-in-the-Loop (HITL) capabilities into the Autonomous AI Travel Advisor.

Prior to this phase, the LangGraph workflow executed autonomously from start to finish.

This phase adds user approval before finalizing travel recommendations.

---

## Objectives

- Introduce human oversight
- Enable user validation
- Prevent fully autonomous execution
- Support approval-based workflows
- Prepare for enterprise governance

---

## Workflow

START

↓

Research Agent

↓

Budget Agent

↓

Hotel Agent

↓

Itinerary Agent

↓

Risk Agent

↓

Supervisor Agent

↓

Approval Node

↓

User Decision

↓

Approve?

├── YES → END

└── NO → Regenerate Workflow

---

## Components Implemented

### Approval Manager

File:

```text
human_loop/approval_manager.py
```

Responsibilities:

- Capture user approval
- Validate decision input
- Return workflow action

---

### Approval Node

File:

```text
graph/nodes.py
```

Responsibilities:

- Pause execution
- Request approval
- Update workflow state

---

### Approval State

Added to TravelState:

```python
approval_status: str
```

Purpose:

Store user decision inside the graph state.

---

## Conditional Routing

Implemented using:

```python
builder.add_conditional_edges()
```

Routing Logic:

### Approved

```text
Approval Node
      ↓
END
```

### Rejected

```text
Approval Node
      ↓
Supervisor Agent
      ↓
Approval Node
```

---

## Benefits

- Human oversight
- Increased reliability
- User-controlled execution
- Enterprise AI governance
- Reduced automation risks

---

## Logging

Approval decisions are logged:

```python
logger.info(
    f"Approval Decision: {decision}"
)
```

---

## Validation

Tested Scenarios:

### Approval Path

Input:

```text
yes
```

Output:

Workflow completed successfully.

---

### Rejection Path

Input:

```text
no
```

Output:

Workflow regenerated.

---

## Architecture Impact

Before:

User

↓

LangGraph

↓

END

After:

User

↓

LangGraph

↓

Approval Node

↓

Decision

↓

Conditional Routing

↓

END

---

## Future Enhancements

- LangGraph Interrupts
- API-based approvals
- React approval interface
- n8n approval workflows
- Email approval links
- Slack approvals
- Multi-level approval chains

---

## Outcome

The system now supports Human-in-the-Loop workflows, enabling users to review and approve AI-generated travel recommendations before completion.