# 📘 Day 2: Git and Terminal Usage
### Module 0: Prerequisites | ⏱️ 1 Hour Total

> **Goal**: Master the terminal and Git so you can manage every line of code in your AI agent projects like a professional.

---

## ⏱️ Part 1: Learn (30 minutes)

---

### 2.1 Why This Matters for Agentic AI

Every professional AI project needs:
- **Terminal**: To run scripts, install packages, start servers, and debug agents
- **Git**: To track changes, undo mistakes, collaborate, and deploy

```
Without Git:
  "I broke something... which file did I change? When? What was the old code?"
  → PANIC

With Git:
  git log       → See exactly what changed and when
  git diff      → See what's different right now
  git revert    → Undo any mistake instantly
  → CALM
```

> Agents run in terminals. Agent code lives in Git repos. No exceptions.

---

### 2.2 Terminal Basics — Your Command Center

The terminal (also called CLI / Command Line / Shell) is where you'll:
- Run Python scripts (`python agent.py`)
- Install packages (`pip install langchain`)
- Start servers (`python -m http.server`)
- Manage files and folders

#### Essential Commands:

| Command (Windows) | What It Does | Example |
|-------------------|-------------|---------|
| `cd folder_name` | Change directory (go into a folder) | `cd "Agentic Ai"` |
| `cd ..` | Go up one level | `cd ..` |
| `dir` | List files in current folder | `dir` |
| `mkdir name` | Create a new folder | `mkdir my_agent` |
| `type file.txt` | Show file contents | `type README.md` |
| `echo text > file` | Write text to a file | `echo Hello > readme.txt` |
| `del file.txt` | Delete a file | `del old_script.py` |
| `cls` | Clear the terminal screen | `cls` |
| `python script.py` | Run a Python file | `python day1_lab.py` |
| `pip install pkg` | Install a Python package | `pip install requests` |
| `pip list` | See installed packages | `pip list` |

#### PowerShell Bonus Commands:

| Command | What It Does | Example |
|---------|-------------|---------|
| `Get-Location` | Show current path (like `pwd`) | `Get-Location` |
| `Set-Location` | Change directory (like `cd`) | `Set-Location Desktop` |
| `Get-ChildItem` | List items (like `dir`/`ls`) | `Get-ChildItem -Recurse` |
| `New-Item` | Create file or folder | `New-Item -Type File test.py` |
| `Remove-Item` | Delete file or folder | `Remove-Item old.py` |

---

### 2.3 Git — The Time Machine for Your Code

Git tracks **every change** you make to your code. Think of it as:
- **Save points** in a video game — you can always go back
- **Track changes** in Word — but for code, and way more powerful

#### The 3 Stages of Git:

```
┌─────────────────────────────────────────────────────────┐
│                    GIT WORKFLOW                          │
│                                                          │
│  ┌───────────┐    git add    ┌───────────┐   git commit │
│  │  WORKING  │ ───────────>  │  STAGING  │ ──────────>  │
│  │ DIRECTORY │               │   AREA    │              │
│  │           │               │           │   ┌────────┐ │
│  │ (your     │               │ (ready to │   │ LOCAL  │ │
│  │  files)   │               │  commit)  │   │ REPO   │ │
│  │           │               │           │   │(.git)  │ │
│  └───────────┘               └───────────┘   └────────┘ │
│                                                    │     │
│                                              git push    │
│                                                    │     │
│                                              ┌─────▼───┐ │
│                                              │ REMOTE  │ │
│                                              │ (GitHub)│ │
│                                              └─────────┘ │
└─────────────────────────────────────────────────────────┘
```

**In simple words:**
1. **Working Directory** — You edit files normally
2. **Staging Area** — You pick which changes to save (`git add`)
3. **Local Repo** — You save a snapshot with a message (`git commit`)
4. **Remote** — You upload to GitHub/GitLab (`git push`)

---

### 2.4 Essential Git Commands

#### Setup (One-time):
```bash
# Tell Git who you are
git config --global user.name "Sushant"
git config --global user.email "your@email.com"
```

#### Starting a Project:
```bash
# Initialize Git in your project folder
git init

# Check the status — what's changed?
git status
```

#### The Daily Workflow (you'll do this EVERY DAY):
```bash
# 1. Check what's changed
git status

# 2. Stage specific files (pick what to save)
git add day1_lab.py
git add my_progress.json

# OR stage everything at once
git add .

# 3. Commit (save a snapshot with a message)
git commit -m "Day 1: Complete lab task - API caller with retry logic"

# 4. View your history
git log --oneline
```

#### Undoing Mistakes:
```bash
# Undo changes to a file (before staging)
git checkout -- filename.py

# Unstage a file (after git add, before commit)
git reset HEAD filename.py

# Undo the last commit (keep the changes)
git reset --soft HEAD~1

# See what changed in a file
git diff filename.py
```

---

### 2.5 Branching — Work on Features Without Breaking Main Code

Branches let you experiment safely:

```
main:     A ─── B ─── C ─── D ─── E (stable code)
                 \                 ↑
feature:          F ─── G ─── H ──┘ (merge when ready)
```

```bash
# Create and switch to a new branch
git checkout -b feature/add-memory

# List all branches (* = current)
git branch

# Switch between branches
git checkout main

# Merge a branch back into main
git checkout main
git merge feature/add-memory

# Delete a branch after merging
git branch -d feature/add-memory
```

#### Why Branching Matters for AI Agents:
```
main               → stable, working agent
feature/add-rag    → experimenting with RAG memory
feature/new-tools  → adding new tools
fix/retry-bug      → fixing a bug in retry logic
```
You can experiment without fear. If it breaks, just switch back to `main`.

---

### 2.6 .gitignore — What NOT to Track

Some files should NEVER be in Git:

```bash
# Create a .gitignore file
# These files/folders will be ignored by Git

# API keys and secrets (CRITICAL!)
.env
secrets.json
*_key.txt

# Python
__pycache__/
*.pyc
*.pyo
venv/
.venv/

# IDE files
.vscode/
.idea/

# OS files
Thumbs.db
.DS_Store

# Large model files
*.bin
*.pt
*.safetensors

# Logs
*.log
```

> **CRITICAL**: Never commit API keys, passwords, or secrets to Git.
> If you accidentally push an OpenAI key to GitHub, bots will find it
> within minutes and rack up thousands of dollars in charges.

---

### 2.7 Project Structure for AI Agents

Set up your Agentic AI project like a professional from Day 1:

```
Agentic Ai/
├── .git/                  # Git repository (auto-created)
├── .gitignore             # Files to ignore
├── .env                   # API keys (NEVER commit this!)
├── README.md              # Project description
├── requirements.txt       # Python dependencies
│
├── day1_lab.py            # Day 1 lab work
├── day2_lab.py            # Day 2 lab work
├── my_progress.json       # Your learning progress
│
├── agents/                # Your agent code (future)
│   ├── __init__.py
│   ├── basic_agent.py
│   └── tools.py
│
├── prompts/               # Prompt templates (future)
│   └── system_prompt.txt
│
└── tests/                 # Test files (future)
    └── test_tools.py
```

---

### 2.8 Key Takeaways — Day 2 Cheat Sheet

```
TERMINAL:
  cd folder        → Navigate into folder
  cd ..            → Go up one level
  dir              → List files
  mkdir name       → Create folder
  python file.py   → Run Python script
  pip install pkg  → Install package

GIT DAILY WORKFLOW:
  git status       → What changed?
  git add .        → Stage all changes
  git commit -m "" → Save snapshot
  git log --oneline → View history

GIT BRANCHING:
  git checkout -b name → Create branch
  git checkout main    → Switch to main
  git merge name       → Merge branch

RULES:
  - Commit often with clear messages
  - Never commit API keys or secrets
  - Use branches for experiments
  - Write a .gitignore FIRST
```

---

## ⏱️ Part 2: Daily Lab Task (30 minutes)

### Lab: "Set Up Your Agent Project with Git"

**Objective**: Initialize your Agentic AI project with Git, create a proper structure, and practice the full Git workflow.

### Step-by-Step Instructions:

**Step 1: Initialize Git in your project**
```bash
cd "C:\Users\sushant\Desktop\Agentic Ai"
git init
git status
```

**Step 2: Create a .gitignore file**
Create a file called `.gitignore` with these contents:
```
.env
secrets.json
__pycache__/
*.pyc
venv/
.venv/
.vscode/
.idea/
Thumbs.db
*.log
*.bin
*.pt
```

**Step 3: Create a README.md**
Create a file called `README.md`:
```markdown
# Agentic AI Learning Journey

Learning to build AI agents from scratch — a 45-day curriculum.

## Progress
- [x] Day 1: Backend Basics (HTTP, JSON, APIs)
- [ ] Day 2: Git and Terminal Usage
- [ ] Day 3: REST API Knowledge

## Tech Stack
- Python 3.12
- requests library

## Author
Sushant
```

**Step 4: Create a requirements.txt**
```
requests
```

**Step 5: Create project folders**
```bash
mkdir agents
mkdir prompts
mkdir tests
```

**Step 6: Make your first commit**
```bash
git add .
git status
git commit -m "Day 1: Initialize project with lab solution and progress tracking"
```

**Step 7: Create a branch, make a change, merge it**
```bash
# Create a branch
git checkout -b feature/day2-setup

# Update README.md — mark Day 2 as complete:
#   - [x] Day 2: Git and Terminal Usage

# Commit the change
git add README.md
git commit -m "Day 2: Mark git and terminal lesson as complete"

# Switch back to main and merge
git checkout main
git merge feature/day2-setup

# View your history
git log --oneline
```

**Step 8: Create `day2_lab.py`**
Write a simple Python script that reads and prints your git log:
```python
import subprocess
import json

# Run git log and capture output
result = subprocess.run(
    ["git", "log", "--oneline", "--all"],
    capture_output=True, text=True
)

print("Git History:")
print(result.stdout)

# Update progress
with open("my_progress.json", "r") as f:
    progress = json.load(f)

progress["current_day"] = 2
progress["skills_learned"].extend([
    "Terminal/CLI commands",
    "Git init, add, commit, log",
    "Git branching and merging",
    ".gitignore for secrets",
    "Project structure for AI agents"
])

with open("my_progress.json", "w") as f:
    json.dump(progress, f, indent=2)

print("\nProgress updated! Now on Day 2.")
```

---

### Completion Checklist

- [ ] Git is initialized in my project folder
- [ ] .gitignore file exists with proper entries
- [ ] README.md exists with my progress
- [ ] requirements.txt exists
- [ ] agents/, prompts/, tests/ folders created
- [ ] First commit made with a clear message
- [ ] Created a branch, made a change, merged it
- [ ] git log shows at least 2 commits
- [ ] day2_lab.py runs and updates my_progress.json

---

### Coming Tomorrow — Day 3

**REST API Knowledge** — Deep dive into API design, endpoints, authentication (API keys, OAuth, Bearer tokens), request/response patterns, and pagination. You'll build a mini API client that can talk to any REST API — the exact skill needed to connect agents to external services.

---

> *"Code without version control is like writing in sand — one wave and it's gone."* 🌊
> Complete the lab and share your `git log --oneline` output with me!
