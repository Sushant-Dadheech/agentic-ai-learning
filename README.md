# 🤖 Agentic AI Learning Journey

> Learning to build AI agents from scratch — a 45-day structured curriculum covering everything from HTTP basics to production-grade multi-agent systems.

![Progress](https://img.shields.io/badge/Progress-Day%202%2F45-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🗺️ Curriculum Roadmap

Based on the [roadmap.sh AI Agents Roadmap](https://roadmap.sh/ai-agents) — 10 modules, 45 sessions.

| Module | Topic | Days | Status |
|--------|-------|------|--------|
| 0 | **Prerequisites** | 1–3 | 🟡 In Progress |
| 1 | LLM Fundamentals | 4–10 | ⬜ Not Started |
| 2 | AI Agents 101 | 11–14 | ⬜ Not Started |
| 3 | Loop Engineering | 15–17 | ⬜ Not Started |
| 4 | Tools / Actions + MCP | 18–21 | ⬜ Not Started |
| 5 | Agent Memory | 22–25 | ⬜ Not Started |
| 6 | Agent Architectures | 26–29 | ⬜ Not Started |
| 7 | Building Agents | 30–36 | ⬜ Not Started |
| 8 | Evaluation & Testing | 37–39 | ⬜ Not Started |
| 9 | Debugging & Monitoring | 40–41 | ⬜ Not Started |
| 10 | Security & Ethics | 42–44 | ⬜ Not Started |

---

## 📅 Daily Progress

### Module 0: Prerequisites

| Day | Topic | Lab Task | Status |
|-----|-------|----------|--------|
| 1 | Basic Backend Development | API caller with retry logic | ✅ Complete |
| 2 | Git and Terminal Usage | Project setup with Git workflow | ✅ Complete |
| 3 | REST API Knowledge | - | ⬜ Upcoming |

---

## 🔬 Lab Projects

### Day 1: Build Your First API Caller
**File:** [`day1_lab.py`](day1_lab.py)

Built a Python script demonstrating the foundational patterns every AI agent uses:
- **GET requests** — Fetching data from external APIs
- **POST requests** — Sending data (same pattern as calling GPT/Gemini)
- **Error handling** — Gracefully handling 404, 500, 429 errors
- **Retry logic** — Exponential backoff for rate-limited APIs
- **JSON processing** — Reading, writing, and parsing JSON data

> 💡 **Key Insight:** Every AI agent is fundamentally: `Send prompt → Get response → Process result → Decide next action`

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Libraries:** requests, json (stdlib)
- **Version Control:** Git + GitHub
- **Coming Soon:** LangChain, OpenAI API, Gemini API, ChromaDB, CrewAI

---

## 📂 Project Structure

```
agentic-ai-learning/
├── .gitignore              # Files to ignore (API keys, cache, etc.)
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── my_progress.json        # Learning progress tracker
│
├── day1_lab.py             # Day 1: API caller with retry logic
├── day2_lab.py             # Day 2: Git workflow automation
│
├── agents/                 # AI agent code (future)
├── prompts/                # Prompt templates (future)
└── tests/                  # Test suites (future)
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Sushant-Dadheech/agentic-ai-learning.git
cd agentic-ai-learning

# Install dependencies
pip install -r requirements.txt

# Run any day's lab
python day1_lab.py
python day2_lab.py
```

---

## 📖 About This Journey

I'm learning Agentic AI through a structured 45-day curriculum that covers:
- **Foundations:** HTTP, APIs, Git, Python
- **LLM Skills:** Transformers, tokenization, prompt engineering, RAG
- **Agent Core:** Agent loop, tool use, memory, planning
- **Building:** From scratch + frameworks (LangChain, CrewAI, AutoGen)
- **Production:** Testing, monitoring, security, deployment

Following along? Star ⭐ this repo and follow my progress!

---

## 🔗 Connect

- **LinkedIn:** [https://www.linkedin.com/in/sushant-dadheech-007a53329/]

*Built with dedication, one day at a time.* 🧱
