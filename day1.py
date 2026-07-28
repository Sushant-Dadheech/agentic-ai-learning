import requests 
import json
import time 

def get_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            joke = response.json()
            
            print(f"\n Status Code {response.status_code} (Success!) ")
            print(f"   Type: {joke['type']} ")
            print(f"  Setup: {joke['setup']}")
            print(f"  Punchline: {joke['punchline']}")
            print(f"\n  Raw JSON response:")
            print(f" {json.dumps(joke, indent=4)} ")
        else:
            print(f"\/ unexpected status code: {response.status_code}")
            print(f"  Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("\n Error: could not connect to the api.")
        print("   Possible causes: API is down, no internet connection.")
        
    except requests.exceptions.Timeout:
        print("Error: request time out please try again after 10seconds")
    except requests.exceptions.RequestException as e:
        print(f"\n  ERROR: An unexpected error occurred: {e}")
        
def post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    payload = {
        "title": "My Agentic Ai journey",
        "body": "Day 1: Learning backend basics"
        "userId": 1
    }    
    
    headers = {
        "Content-type": "application/json"

    }
    
    try:
        response = requests.post(url, timeout=10)
        print(f"\n Status Code {response.status_code}")
        if response.status_code == 201:
            joke = response.json()
            print(f" Result: Post Created successfully!")
            print(f"  Assigned ID: {joke.get('id')}")
            print(f"  Title: {joke.get('title')}")
            print(f"  Body: {joke.get('body')}")
            print(f"  User ID: {joke.get('userId')}")
            print(f"\n   Full JSON response:")
            print(f"{json.dumps(data, indent=4)}")
        else:
            print(f"  Unexpected response: {response.text}")
    except requests.exceptions.ConnectionError:
        print(f"Error: {e}")
    print()
    
    print("  --- AGENT PARALLEL ---")
    print("  Calling an LLM API uses the EXACT same pattern:")
    print("  POST https://api.openai.com/v1/chat/completions")
    print("  Headers: Authorization: Bearer sk-...")
    print("  Body: {model: 'gpt-4o', messages: [...]}")
    print("  Response: {choices: [{message: {content: '...'}}]}")
    print()

