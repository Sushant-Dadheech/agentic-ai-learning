"""
=============================================================
DAY 1 LAB TASK: "Build Your First API Caller"
=============================================================
Agentic AI & Chatbot Automation - Master Curriculum
Student: Sushant
Date: July 2026

This script demonstrates the foundational patterns that
EVERY AI agent uses: HTTP requests, JSON processing,
and error handling with retry logic.
=============================================================
"""

import requests
import json
import time


# ═══════════════════════════════════════════════════════════
# TASK 1: GET Request — Fetch a Random Joke
# ═══════════════════════════════════════════════════════════
# WHY THIS MATTERS: AI agents use GET requests to FETCH data
# from external sources — weather APIs, search engines,
# databases, knowledge bases, etc.
# ═══════════════════════════════════════════════════════════

def task1_get_request():
    """Fetch a random joke from a public API using GET request."""
    print("=" * 60)
    print("TASK 1: GET Request — Fetch a Random Joke")
    print("=" * 60)

    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        # Send GET request to the API
        response = requests.get(url, timeout=10)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            joke = response.json()

            # Extract specific fields from the JSON
            print(f"\n  Status Code: {response.status_code} (Success!)")
            print(f"  Type: {joke['type']}")
            print(f"  Setup: {joke['setup']}")
            print(f"  Punchline: {joke['punchline']}")
            print(f"\n  Raw JSON response:")
            print(f"  {json.dumps(joke, indent=4)}")
        else:
            print(f"\n  Unexpected status code: {response.status_code}")
            print(f"  Response: {response.text}")

    except requests.exceptions.ConnectionError:
        # This happens when the API is down or you have no internet
        print("\n  ERROR: Could not connect to the API.")
        print("  Possible causes: API is down, no internet connection.")

    except requests.exceptions.Timeout:
        # This happens when the API takes too long to respond
        print("\n  ERROR: Request timed out after 10 seconds.")

    except requests.exceptions.RequestException as e:
        # Catch-all for any other request errors
        print(f"\n  ERROR: An unexpected error occurred: {e}")

    print()


# ═══════════════════════════════════════════════════════════
# TASK 2: POST Request — Create a Fake Post
# ═══════════════════════════════════════════════════════════
# WHY THIS MATTERS: AI agents use POST requests to SEND data
# to APIs — this is EXACTLY how you send prompts to GPT,
# Gemini, or Claude. The pattern is identical!
# ═══════════════════════════════════════════════════════════

def task2_post_request():
    """Send data to a fake API using POST request."""
    print("=" * 60)
    print("TASK 2: POST Request — Create a Fake Post")
    print("=" * 60)

    url = "https://jsonplaceholder.typicode.com/posts"

    # This is the data we're sending — similar to how you'd
    # send a prompt to an LLM API
    payload = {
        "title": "My Agentic AI Journey",
        "body": "Day 1: Learning backend basics — HTTP, JSON, APIs. "
                "This is the foundation for building AI agents.",
        "userId": 1
    }

    # Headers tell the server what format the data is in
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Send POST request with JSON body
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        print(f"\n  Status Code: {response.status_code}")

        if response.status_code == 201:  # 201 = Created
            data = response.json()
            print(f"  Result: Post created successfully!")
            print(f"  Assigned ID: {data.get('id')}")
            print(f"  Title: {data.get('title')}")
            print(f"  Body: {data.get('body')}")
            print(f"  User ID: {data.get('userId')}")
            print(f"\n  Full JSON response:")
            print(f"  {json.dumps(data, indent=4)}")
        else:
            print(f"  Unexpected response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"\n  ERROR: {e}")

    print()

    # AGENT PARALLEL: This is how calling an LLM looks:
    print("  --- AGENT PARALLEL ---")
    print("  Calling an LLM API uses the EXACT same pattern:")
    print("  POST https://api.openai.com/v1/chat/completions")
    print("  Headers: Authorization: Bearer sk-...")
    print("  Body: {model: 'gpt-4o', messages: [...]}")
    print("  Response: {choices: [{message: {content: '...'}}]}")
    print()


# ═══════════════════════════════════════════════════════════
# TASK 3: Error Handling — Handle Different HTTP Errors
# ═══════════════════════════════════════════════════════════
# WHY THIS MATTERS: AI agents WILL encounter errors.
# Rate limits (429), server errors (500), bad requests (400).
# An agent that can't handle errors is an agent that CRASHES.
# ═══════════════════════════════════════════════════════════

def task3_error_handling():
    """Handle different HTTP error codes gracefully."""
    print("=" * 60)
    print("TASK 3: Error Handling — Handling HTTP Errors")
    print("=" * 60)

    # --- Test 1: 404 Not Found ---
    print("\n  --- Test 3a: 404 Not Found ---")
    try:
        response = requests.get("https://httpstat.us/404", timeout=10)
        print(f"  Status Code: {response.status_code}")
        print(f"  Meaning: Resource Not Found")
        print(f"  Agent Action: Check the URL/endpoint. It's wrong or the resource doesn't exist.")
    except requests.exceptions.RequestException as e:
        print(f"  Connection Error: {e}")

    # --- Test 2: 500 Internal Server Error ---
    print("\n  --- Test 3b: 500 Internal Server Error ---")
    try:
        response = requests.get("https://httpstat.us/500", timeout=10)
        print(f"  Status Code: {response.status_code}")
        print(f"  Meaning: Internal Server Error")
        print(f"  Agent Action: Not our fault! Wait and retry. The server has a problem.")
    except requests.exceptions.RequestException as e:
        print(f"  Connection Error: {e}")

    # --- Test 3: 429 Rate Limited (with RETRY LOGIC) ---
    print("\n  --- Test 3c: 429 Rate Limited (with Retry Logic) ---")
    print("  This is the MOST IMPORTANT error to handle for AI agents!")
    print()

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get("https://httpstat.us/429", timeout=10)
            print(f"  Attempt {attempt + 1}/{max_retries}:")
            print(f"    Status Code: {response.status_code}")

            if response.status_code == 429:
                # Exponential backoff: wait longer each time
                # Attempt 1: wait 1s, Attempt 2: wait 2s, Attempt 3: wait 4s
                wait_time = 2 ** attempt
                print(f"    Rate Limited! Waiting {wait_time} second(s) before retry...")

                if attempt < max_retries - 1:
                    time.sleep(wait_time)  # Actually wait
                else:
                    print(f"    Max retries ({max_retries}) exhausted. Giving up.")
                    print(f"    Agent Action: Log this failure, notify the user, try alternative.")
            else:
                print(f"    Success on attempt {attempt + 1}!")
                break

        except requests.exceptions.RequestException as e:
            print(f"  Attempt {attempt + 1} failed with error: {e}")

    print()
    print("  KEY TAKEAWAY: Exponential backoff (1s, 2s, 4s, 8s...)")
    print("  prevents you from hammering the API and getting banned.")
    print()


# ═══════════════════════════════════════════════════════════
# TASK 4: JSON Processing — Save & Load Progress
# ═══════════════════════════════════════════════════════════
# WHY THIS MATTERS: Agents need to READ configuration,
# STORE results, and TRACK state. JSON is the universal
# format for all of this.
# ═══════════════════════════════════════════════════════════

def task4_json_processing():
    """Create, save, read, and display a JSON profile."""
    print("=" * 60)
    print("TASK 4: JSON Processing — Save & Load Progress")
    print("=" * 60)

    # Step 1: Create a Python dictionary (your profile)
    my_profile = {
        "name": "Sushant",
        "goal": "Become an Agentic AI expert",
        "current_day": 1,
        "total_days": 45,
        "module": "Module 0: Prerequisites",
        "skills_learned": [
            "HTTP request/response cycle",
            "GET and POST methods",
            "JSON data format",
            "HTTP status codes (200, 201, 400, 401, 404, 429, 500)",
            "Python requests library",
            "Error handling with try/except",
            "Retry logic with exponential backoff",
            "Reading and writing JSON files"
        ],
        "confidence_level": 7,
        "tasks_completed": {
            "task1_get_request": True,
            "task2_post_request": True,
            "task3_error_handling": True,
            "task4_json_processing": True
        },
        "notes": "Every AI agent is fundamentally: send prompt -> get response -> use result. "
                 "The patterns I learned today are the EXACT same patterns used in production agents.",
        "next_lesson": "Day 2: Git and Terminal Usage"
    }

    # Step 2: Save to a JSON file
    output_file = "my_progress.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(my_profile, f, indent=2, ensure_ascii=False)
    print(f"\n  Saved profile to: {output_file}")

    # Step 3: Read it back from the file
    with open(output_file, "r", encoding="utf-8") as f:
        loaded_profile = json.load(f)

    # Step 4: Display it formatted
    print(f"\n  --- Loaded Profile ---")
    print(f"  Name: {loaded_profile['name']}")
    print(f"  Goal: {loaded_profile['goal']}")
    print(f"  Progress: Day {loaded_profile['current_day']}/{loaded_profile['total_days']}")
    print(f"  Module: {loaded_profile['module']}")
    print(f"  Confidence: {loaded_profile['confidence_level']}/10")
    print(f"  Skills Learned ({len(loaded_profile['skills_learned'])}):")
    for i, skill in enumerate(loaded_profile['skills_learned'], 1):
        print(f"    {i}. {skill}")
    print(f"  Next Lesson: {loaded_profile['next_lesson']}")

    # Step 5: Show the raw JSON (pretty-printed)
    print(f"\n  --- Raw JSON Content ---")
    print(json.dumps(loaded_profile, indent=2))
    print()


# ═══════════════════════════════════════════════════════════
# BONUS: The Retry Pattern You'll Use in Every Agent
# ═══════════════════════════════════════════════════════════

def call_api_with_retry(url, method="GET", headers=None, payload=None, max_retries=3):
    """
    Production-grade API caller with retry logic.
    
    THIS IS THE EXACT PATTERN used in real AI agents when
    calling LLM APIs (OpenAI, Gemini, Claude).
    
    Args:
        url: The API endpoint to call
        method: HTTP method (GET or POST)
        headers: Request headers (dict)
        payload: Request body for POST (dict)
        max_retries: Maximum number of retry attempts
    
    Returns:
        dict: Parsed JSON response
    
    Raises:
        Exception: If all retries are exhausted
    """
    for attempt in range(max_retries):
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=30)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=payload, timeout=30)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            # Success!
            if response.status_code in (200, 201):
                return response.json()

            # Rate limited — wait and retry
            elif response.status_code == 429:
                wait_time = 2 ** attempt
                print(f"  [Retry] Rate limited. Waiting {wait_time}s... "
                      f"(attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue

            # Auth error — don't retry, it won't help
            elif response.status_code == 401:
                raise Exception("Authentication failed! Check your API key.")

            # Client error — don't retry
            elif 400 <= response.status_code < 500:
                raise Exception(f"Client error {response.status_code}: {response.text}")

            # Server error — retry
            elif response.status_code >= 500:
                wait_time = 2 ** attempt
                print(f"  [Retry] Server error {response.status_code}. "
                      f"Waiting {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue

        except requests.exceptions.ConnectionError:
            wait_time = 2 ** attempt
            print(f"  [Retry] Connection failed. Waiting {wait_time}s... "
                  f"(attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)

        except requests.exceptions.Timeout:
            wait_time = 2 ** attempt
            print(f"  [Retry] Request timed out. Waiting {wait_time}s... "
                  f"(attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)

    raise Exception(f"Max retries ({max_retries}) exhausted for {url}")


# ═══════════════════════════════════════════════════════════
# MAIN — Run All Tasks
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print()
    print("*" * 60)
    print("*  DAY 1 LAB: Build Your First API Caller               *")
    print("*  Agentic AI & Chatbot Automation Curriculum            *")
    print("*" * 60)
    print()

    # Run all 4 tasks
    task1_get_request()
    task2_post_request()
    task3_error_handling()
    task4_json_processing()

    # Summary
    print("=" * 60)
    print("LAB COMPLETE!")
    print("=" * 60)
    print()
    print("  CHECKLIST:")
    print("  [x] Task 1: GET request — fetched data from an API")
    print("  [x] Task 2: POST request — sent data to an API")
    print("  [x] Task 3: Error handling — handled 404, 500, 429")
    print("  [x] Task 4: JSON processing — saved/loaded my_progress.json")
    print()
    print("  KEY PATTERNS LEARNED:")
    print("  1. requests.get()  — Fetch data (agent reads from tools)")
    print("  2. requests.post() — Send data (agent calls LLM APIs)")
    print("  3. response.json() — Parse response (agent reads results)")
    print("  4. try/except      — Handle errors (agent stays alive)")
    print("  5. Exponential backoff — Retry smartly (agent is resilient)")
    print("  6. json.dump/load  — Save/read state (agent has memory)")
    print()
    print("  NEXT: Day 2 — Git and Terminal Usage")
    print()
