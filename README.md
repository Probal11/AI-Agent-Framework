# AI Agent Framework

A lightweight **AI Agent Framework** built in Python that allows defining, orchestrating, and executing **multi-agent workflows**. The framework supports task dependencies, shared memory, retries, and audit logging, without relying on existing agent frameworks like CrewAI, AutoGen, or n8n.

---


This framework lets you:

* Create multiple AI agents with different roles
* Define a workflow where each agent does a specific task
* Run those tasks in the correct order
* Share information between agents
* Handle failures with retries
* Log everything for monitoring and auditing

Instead of one AI doing everything, **multiple AIs work together**, step by step.

---

## ✨ Key Features

* 🧠 Multiple AI agents with defined roles
* 🔁 Workflow orchestration using task dependencies (DAG-style)
* 🗂 Shared state and memory between agents
* 🔄 Automatic retries and timeout handling
* 📝 Structured audit logs for observability
* 🔌 Model-agnostic design (uses Google Gemini by default)
* 🧩 Easy to extend with tools, APIs, or human-in-the-loop steps

---

## 🏗 Architecture Overview

```
Input (CLI / API-ready)
        ↓
Workflow Orchestrator
        ↓
Agent Executors (Gemini LLM)
        ↓
Shared State / Memory
        ↓
Audit Logs
```

---

## 📂 Project Structure

```
.
├── core/
│   ├── agent.py        # Agent logic (LLM calls, retries, guardrails)
│   ├── workflow.py     # Workflow orchestrator
│   ├── task.py         # Task nodes and dependencies
│   ├── state.py        # Shared memory/state store
│   └── audit.py        # Audit logging
│
├── ingress/            # input handlers
├── main.py             # Example workflow execution
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🤖 Agents

Each agent:

* Has a **role** (e.g., Researcher, Writer, Reviewer)
* Uses an LLM (Gemini) to perform tasks
* Supports retries and error handling
* Logs every execution step

Example agents included:

* **Researcher** – gathers information
* **Writer** – generates content
* **Reviewer** – reviews and improves output

---

## 🔁 Workflow Execution

Workflows are defined as **task graphs**:

* Each task can depend on other tasks
* Tasks only run when dependencies are complete
* Outputs are stored in shared memory and passed forward

This ensures:

* Correct execution order
* Reliability
* Easy debugging

---

## 🧪 Example Workflow

The demo workflow performs:

1. Research on a topic
2. Writing a blog post
3. Reviewing and improving the blog post

This demonstrates:

* Multi-agent collaboration
* State passing
* Observability and retries

---

## 🛡 Reliability & Observability

* Automatic retries on failure
* Timeout enforcement
* JSON-based audit logs
* Clear error reporting

All actions are logged for monitoring and debugging.

---
