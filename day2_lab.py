import subprocess
import json
import os

print("\n--- DAY 2 LAB START ---\n")

# Run git log and capture output
print("Fetching Git History...")
try:
    result = subprocess.run(
        ["git", "log", "--oneline", "--all"],
        capture_output=True, text=True, check=True
    )
    print("\nGit History:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Failed to run git log:", e)
except FileNotFoundError:
    print("Git is not installed or not in PATH.")

# Update progress
progress_file = "my_progress.json"

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress = json.load(f)

    progress["current_day"] = 2
    
    # Add new skills if they don't already exist
    new_skills = [
        "Terminal/CLI commands",
        "Git init, add, commit, log",
        "Git branching and merging",
        ".gitignore for secrets",
        "Project structure for AI agents"
    ]
    
    for skill in new_skills:
        if skill not in progress.get("skills_learned", []):
            progress.setdefault("skills_learned", []).append(skill)

    with open(progress_file, "w") as f:
        json.dump(progress, f, indent=2)

    print(f"\nProgress updated! You are now officially on Day 2.")
else:
    print(f"\n{progress_file} not found. Please run Day 1 lab first.")
