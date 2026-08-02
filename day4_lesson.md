# 📘 Day 4: LLM Basics — How AI Agents Think
### Module 1: LLM Fundamentals | ⏱️ 1 Hour Total

> **Goal**: Understand what Large Language Models are, how they work under the hood, and why every concept matters for building AI agents.

---

## ⏱️ Part 1: Learn (30 minutes)

---

### 4.1 What is a Large Language Model (LLM)?

An LLM is a **massive pattern-matching machine** trained on billions of words from the internet. It doesn't "think" — it predicts the most likely next word based on everything it's seen.

```
Input:  "The capital of France is ___"
LLM:    P("Paris") = 97%
        P("Lyon")  = 1.5%
        P("a")     = 0.8%
        P("the")   = 0.3%
        → Picks "Paris"
```

#### The Key Insight:
```
LLM = A very sophisticated autocomplete

Your phone keyboard:    "I'm on my ___" → "way" (basic prediction)
GPT-4o:                 "Explain quantum physics" → (paragraph of accurate text)

Same idea. Wildly different scale.
  Phone:  Trained on YOUR texts (~100K words)
  GPT-4o: Trained on INTERNET (~13 TRILLION tokens)
```

#### Popular LLMs You'll Work With:

| Model | Company | Size | Best For |
|-------|---------|------|----------|
| GPT-4o | OpenAI | ~1.8T params | General purpose, coding, reasoning |
| GPT-4o-mini | OpenAI | Smaller | Fast, cheap, good enough for most tasks |
| Gemini 2.5 Pro | Google | Large | Long context, multimodal |
| Claude 4 | Anthropic | Large | Safety, long documents, coding |
| Llama 3.1 | Meta | 8B-405B | Open source, run locally |
| Mistral | Mistral AI | 7B-Large | Open source, efficient |

---

### 4.2 Neural Networks — The 60-Second Version

You don't need to be a math PhD. Here's what matters:

```
INPUT          HIDDEN LAYERS         OUTPUT
(your text)    (pattern matching)    (next word)

"The cat"  →  [layer1] → [layer2] → ... → [layer96]  →  "sat"
               ↑
               These layers learn PATTERNS:
               Layer 1:  Letters, basic words
               Layer 10: Grammar, sentence structure  
               Layer 50: Facts, reasoning
               Layer 96: Complex understanding
```

**Key terms:**
- **Parameters**: The "knobs" the model learned to tune (GPT-4 has ~1.8 trillion)
- **Weights**: The values of those knobs (learned during training)
- **Training**: Showing the model billions of text examples so it learns patterns
- **Inference**: Using the trained model to generate new text (this is what you do)

> **For agents, you only care about INFERENCE** — sending prompts and getting responses. You don't need to train models.

---

### 4.3 The Transformer Architecture — Why It Changed Everything

Before 2017, AI models read text one word at a time (slow, forgetful).
The **Transformer** (invented by Google) reads ALL words at once.

```
OLD (RNN/LSTM):
  "The" → process → "cat" → process → "sat" → process → "on" → process
  (Sequential — slow, forgets beginning by the end)

NEW (Transformer):
  "The cat sat on the mat"
   ↓    ↓   ↓   ↓   ↓   ↓
  [ALL PROCESSED SIMULTANEOUSLY]
  (Parallel — fast, remembers everything)
```

#### The Secret Weapon: Attention Mechanism

Attention answers: **"Which words should I focus on right now?"**

```
"The animal didn't cross the road because it was too tired"

What does "it" refer to?

Attention scores:
  "it" → "animal"  = 0.85  ← HIGH (correct!)
  "it" → "road"    = 0.10
  "it" → "cross"   = 0.03
  "it" → "the"     = 0.02

The model LEARNS to pay attention to the right words.
```

#### Self-Attention in One Sentence:
> Every word looks at every other word and asks: "How relevant are you to understanding me?"

---

### 4.4 Tokens — The Language of LLMs

LLMs don't read words — they read **tokens**. A token is a chunk of text (roughly 3/4 of a word).

```
TOKENIZATION EXAMPLES:

"Hello world"           → ["Hello", " world"]                    = 2 tokens
"I'm learning AI"       → ["I", "'m", " learning", " AI"]       = 4 tokens  
"Tokenization"          → ["Token", "ization"]                   = 2 tokens
"GPT-4o is amazing!"    → ["G", "PT", "-", "4", "o", " is"...]  = ~7 tokens
```

#### Why Tokens Matter:

```
1. COST: You pay per token
   GPT-4o: $2.50 per 1M input tokens, $10 per 1M output tokens
   1000 tokens ≈ 750 words ≈ 1.5 pages of text

2. CONTEXT WINDOW: Max tokens the model can see at once
   GPT-4o:        128,000 tokens (~96,000 words = a full novel)
   Gemini 2.5:  1,000,000 tokens (~750,000 words = 10 novels!)
   Claude 4:      200,000 tokens (~150,000 words)

3. SPEED: More tokens = slower response
   100 tokens  → instant
   4000 tokens → 2-5 seconds
```

#### Token Counting Rule of Thumb:
```
English:  1 token ≈ 4 characters ≈ 0.75 words
Code:     1 token ≈ 3 characters (code uses more tokens)
Numbers:  Each digit can be its own token! "2026" = up to 2-3 tokens
```

---

### 4.5 Embeddings — How LLMs Understand Meaning

An **embedding** is a list of numbers that represents the MEANING of text.

```
"king"  → [0.2, 0.8, 0.1, 0.9, ...]   (1536 numbers)
"queen" → [0.2, 0.8, 0.9, 0.9, ...]   (similar! both royalty)
"cat"   → [0.7, 0.1, 0.3, 0.2, ...]   (very different)
```

#### The Famous Example:
```
king - man + woman ≈ queen

[0.2, 0.8, 0.1, 0.9]     (king)
- [0.1, 0.3, 0.1, 0.4]   (man)
+ [0.1, 0.3, 0.9, 0.4]   (woman)
= [0.2, 0.8, 0.9, 0.9]   ≈ queen!
```

#### Why Embeddings Matter for Agents:

```
SEARCH:     Convert question to embedding → find similar documents
MEMORY:     Store past conversations as embeddings → recall relevant ones
RAG:        Embed documents → when user asks question → find matching docs
SIMILARITY: Compare two texts → are they about the same topic?
```

> You'll use embeddings heavily in Module 5 (Agent Memory) and when building RAG systems.

---

### 4.6 Temperature & Top-p — Controlling Creativity

These two settings control HOW the model picks the next word:

#### Temperature (0.0 to 2.0):

```
Temperature = 0.0 (Deterministic — always picks the highest probability)
  "The capital of France is ___"
  → "Paris" (every single time)

Temperature = 0.7 (Balanced — some creativity)
  → "Paris" (most times)
  → "a beautiful city called Paris" (sometimes)

Temperature = 1.5 (Creative — more random)
  → "Paris, the city of lights and dreams"
  → "honestly, quite lovely" (unexpected!)
```

#### When to Use What:

| Temperature | Use Case | Agent Scenario |
|-------------|----------|---------------|
| **0.0** | Facts, code, math, data extraction | Tool calls, structured output |
| **0.3-0.5** | Reliable but natural responses | Customer service agent |
| **0.7** | General conversation (default) | Chat assistant |
| **1.0-1.5** | Creative writing, brainstorming | Content generation agent |

#### Top-p (Nucleus Sampling):

```
Top-p = 0.1 → Only consider the top 10% most likely words
Top-p = 0.9 → Consider the top 90% most likely words (default)
Top-p = 1.0 → Consider ALL words
```

> **Rule of thumb**: Adjust temperature OR top-p, not both. For agents, use temperature=0 for tool calls and temperature=0.7 for conversation.

---

### 4.7 Context Window — The Agent's Short-Term Memory

The context window is EVERYTHING the model can see in one request:

```
┌──────────────────────────────────────────────┐
│              CONTEXT WINDOW (128K tokens)     │
│                                              │
│  System Prompt:     ~500 tokens              │
│  "You are a helpful AI agent..."             │
│                                              │
│  Conversation History: ~2000 tokens          │
│  User: "What's the weather?"                 │
│  Assistant: "Let me check..."                │
│  User: "And in Delhi?"                       │
│                                              │
│  Tool Results:      ~1000 tokens             │
│  [weather_api returned: {temp: 35, ...}]     │
│                                              │
│  Current Prompt:    ~100 tokens              │
│  User: "Compare both cities"                 │
│                                              │
│  REMAINING SPACE:   ~124,400 tokens          │
│  (available for the response)                │
└──────────────────────────────────────────────┘
```

#### Context Window Sizes:

| Model | Context Window | Approximate Pages |
|-------|---------------|-------------------|
| GPT-4o | 128K tokens | ~200 pages |
| GPT-4o-mini | 128K tokens | ~200 pages |
| Gemini 2.5 Pro | 1M tokens | ~1500 pages |
| Claude 4 | 200K tokens | ~300 pages |
| Llama 3.1 8B | 128K tokens | ~200 pages |

> **Agent Impact**: Bigger context = agent can remember more conversation history and handle longer documents. But more tokens = more cost and slower responses.

---

### 4.8 The LLM API Call — Putting It All Together

Here's what a REAL LLM API call looks like (you'll do this in the lab):

```python
import requests

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk-your-key-here",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4o-mini",          # Which model
        "messages": [                      # The conversation
            {
                "role": "system",          # Instructions for the AI
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",            # The human's message
                "content": "What is an AI agent?"
            }
        ],
        "temperature": 0.7,                # Creativity level
        "max_tokens": 500                  # Max response length
    }
)

data = response.json()
answer = data["choices"][0]["message"]["content"]
print(answer)
```

#### The 3 Roles in Every LLM Conversation:

```
SYSTEM:    "You are a travel agent specializing in India"
           → Sets the AI's personality and rules (invisible to user)

USER:      "Find me cheap flights to Goa"
           → The human's message

ASSISTANT: "I found 3 options..."
           → The AI's previous responses (conversation history)
```

---

### 4.9 Key Takeaways — Day 4 Cheat Sheet

```
WHAT IS AN LLM:
  A next-word prediction machine trained on the internet.
  It doesn't "know" — it "predicts."

TRANSFORMER:
  Reads all words at once using ATTENTION.
  Attention = "which words matter for understanding this word?"

TOKENS:
  LLMs read tokens, not words. 1 token ≈ 0.75 words.
  You PAY per token. Context window = max tokens per request.

EMBEDDINGS:
  Numbers that represent MEANING. Similar texts = similar numbers.
  Used for search, memory, and RAG in agents.

TEMPERATURE:
  0.0 = factual/deterministic (for tools)
  0.7 = balanced (for chat)
  1.5 = creative (for brainstorming)

API CALL PATTERN:
  POST to endpoint → send model + messages + settings → get response
  This is the SAME pattern from Day 1 (requests.post)!
```

---

## ⏱️ Part 2: Daily Lab Task (30 minutes)

### Lab: "Talk to an LLM API"

**Objective**: Build a Python script that calls a free LLM API to ask questions, experiment with temperature, and analyze token usage.

> We'll use a **free API** so you don't need to pay anything!

### Task 1: Call a Free LLM API
```python
# Use the free Groq API (free tier, very fast)
# Sign up at: https://console.groq.com (free, no credit card)
# Get your API key from the dashboard
#
# OR use the free Google Gemini API:
# Sign up at: https://aistudio.google.com/apikey (free)
#
# Make a simple chat completion request
# Ask: "Explain what an AI agent is in 3 sentences."
```

### Task 2: Experiment with Temperature
```python
# Call the same API 3 times with:
#   temperature = 0.0 (deterministic)
#   temperature = 0.7 (balanced)
#   temperature = 1.5 (creative)
# Ask the same question each time: "Write a one-line description of Python."
# Compare how the 3 responses differ
```

### Task 3: System Prompts — Give the AI a Personality
```python
# Make 3 API calls with different system prompts:
#   1. "You are a pirate. Speak like a pirate."
#   2. "You are a scientist. Be precise and technical."
#   3. "You are a 5-year-old. Explain things simply."
# Ask each one: "What is the internet?"
# See how the same question gets wildly different answers
```

### Task 4: Count Tokens and Calculate Cost
```python
# After each API call, extract from the response:
#   - prompt_tokens (tokens you sent)
#   - completion_tokens (tokens the model generated)
#   - total_tokens
# Calculate the cost based on the model's pricing
# Print a summary table
```

### Task 5: Build a Simple Chat Loop
```python
# Create a while loop that:
#   1. Asks the user for input
#   2. Sends it to the LLM API
#   3. Prints the response
#   4. Keeps conversation history (list of messages)
#   5. Type "quit" to exit
# This is your FIRST chatbot!
```

---

### Completion Checklist

- [ ] Signed up for a free LLM API (Groq or Gemini)
- [ ] Task 1: Successfully called an LLM API
- [ ] Task 2: Compared 3 temperature settings
- [ ] Task 3: Used 3 different system prompts
- [ ] Task 4: Extracted and displayed token usage
- [ ] Task 5: Built a working chat loop
- [ ] Updated my_progress.json to Day 4
- [ ] Pushed day4_lab.py to GitHub

---

### Coming Tomorrow — Day 5

**How LLMs Work Under the Hood** — Deep dive into the transformer architecture: self-attention math, multi-head attention, positional encoding, feed-forward layers, and the training process (pre-training, fine-tuning, RLHF). Understanding this makes you 10x better at prompting.

---

> *"An LLM doesn't know anything. It predicts everything. The magic is that prediction, at scale, looks a lot like understanding."* 🧠
> Get your free API key and build your first chatbot today!
