# Repo Reviewer Agent

An agentic AI system that understands software repositories by reasoning, using tools, and planning autonomously.

Instead of relying on a single LLM prompt, the agent follows the ReAct (Reason → Act → Observe) pattern to inspect codebases, gather information, and produce architecture-level insights.

This project is being built from first principles to understand how modern AI agents work under the hood before introducing frameworks like LangGraph or LangChain.


## Current Capabilities

- Read repository files
- Multi-step reasoning using tool calls
- Generic tool execution via a registry
- Structured responses validated with JSON

---

## Planned Features

### Repository Understanding

- List files
- Search source code
- Read directories recursively
- Parse multiple programming languages

### Intelligent Analysis

- Architecture overview
- Dependency graph generation
- Design pattern detection
- Code quality review
- Security analysis
- Performance suggestions

### Agent Capabilities

- Planning
- Reflection
- Long-term memory
- Multi-tool reasoning
- Self-correction

### Future Integrations

- LangGraph
- LangChain
- MCP (Model Context Protocol)
- GitHub API
- Local repositories
- Vector databases

---

## Project Structure

```text
repo-reviewer-agent/
│
├── src/
│   ├── agent.py
│   ├── schema.py
│   ├── config.py
│   ├── llms/
│   └── tools/
│
├── README.md
├── requirements.txt
└── .env
```

---

## Tech Stack

- Python
- Google Gemini
- Pydantic
- Tenacity

---

## Vision

The goal is to build an AI software architect capable of understanding an unfamiliar codebase the same way an experienced engineer would:

- Explore the repository
- Read relevant files
- Gather evidence
- Plan investigation steps
- Produce well-reasoned architectural insights

Rather than depending on a single prompt, the system incrementally acquires knowledge through tool use and reasoning.

---

## Status

🚧 Active Development

The project currently supports generic tool execution through a ReAct loop. Additional tools, planning, memory, and advanced agent behaviours are under development.