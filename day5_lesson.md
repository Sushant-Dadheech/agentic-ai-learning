# 📘 Day 5: How LLMs Work Under the Hood
### Module 1: LLM Fundamentals | ⏱️ 1 Hour Total

> **Goal**: Understand the Transformer architecture deeply enough that you can reason about WHY models behave the way they do — and use that knowledge to write better prompts and build smarter agents.

---

## ⏱️ Part 1: Learn (30 minutes)

---

### 5.1 The Big Picture — From Text In to Text Out

Before we dive into the parts, here's the FULL pipeline of what happens when you send "What is Python?" to GPT:

```
YOUR TEXT                    INSIDE THE MODEL                         OUTPUT
─────────                    ────────────────                         ──────

"What is     →  Tokenize     →  Embed      →  Transformer Layers  →  Predict
 Python?"       [What]          [0.2,0.8,      × 96 layers            next
                [is]             0.1,...]       (attention +           token
                [Python]        [0.5,0.3,       feed-forward)          ↓
                [?]              0.9,...]                           "Python"
                                    ↑                               "is"
                                    |                               "a"
                              Add position                          "programming"
                              information                           "language"
                                                                    "..."
```

**Each component has a specific job:**

| Step | What It Does | Analogy |
|------|-------------|---------|
| Tokenizer | Splits text into chunks | Breaking a sentence into words |
| Embedding | Converts tokens to numbers | Looking up each word in a dictionary |
| Positional Encoding | Adds word order info | Numbering each word's position |
| Attention | Finds relationships between words | Reading comprehension |
| Feed-Forward | Processes each position | Thinking about what you read |
| Output Layer | Predicts next token | Writing your answer |

---

### 5.2 Step 1: Tokenization — Breaking Text into Pieces

You learned the basics in Day 4. Here's the deeper view:

#### How Tokenizers Are Built (BPE Algorithm):

```
BYTE PAIR ENCODING (BPE) — Used by GPT, Llama, Mistral

Start with individual characters:
  "learning" → ['l', 'e', 'a', 'r', 'n', 'i', 'n', 'g']

Find most frequent pair and merge:
  'i' + 'n' appears most → merge to 'in'
  ['l', 'e', 'a', 'r', 'n', 'in', 'g']

Repeat thousands of times:
  'l' + 'e' → 'le'
  'le' + 'a' → 'lea'
  'lea' + 'r' → 'lear'
  'lear' + 'n' → 'learn'
  'learn' + 'in' → 'learnin'
  'learnin' + 'g' → 'learning'

Final: "learning" → ['learning']  (1 token — common word!)
```

#### Why This Matters for Agents:

```
PROBLEM: "Count the number of 'r's in strawberry"
TOKENS:  ['str', 'aw', 'berry']

The model sees 3 chunks, NOT individual letters!
It can't "see" each 'r' — that's why LLMs are bad at letter counting.

AGENT SOLUTION: Use a Python tool to count letters instead of asking the LLM.
This is WHY agents need tools — LLMs have blind spots.
```

---

### 5.3 Step 2: Embeddings — Converting Tokens to Vectors

Each token gets converted to a **vector** (list of numbers) that captures its meaning:

```
VOCABULARY SIZE: ~100,000 tokens
EMBEDDING DIMENSION: 4096 numbers (for GPT-4 scale)

TOKEN → LOOK UP IN EMBEDDING TABLE → VECTOR

"cat"    → embedding_table[8821]  → [0.23, -0.41, 0.87, ..., 0.12]  (4096 nums)
"dog"    → embedding_table[9134]  → [0.25, -0.38, 0.82, ..., 0.15]  (similar!)
"Python" → embedding_table[31547] → [0.71, 0.22, -0.33, ..., 0.88]  (different)
```

#### The Embedding Space:

```
Imagine a map where similar words are close together:

                    "king" •
                              • "queen"
            "prince" •
                        • "princess"


    "cat" •
            • "dog"
              • "puppy"


                                    "Python" •
                                       • "JavaScript"
                                    • "Java"
```

> Words with similar meanings cluster together. This is how LLMs "understand" that king and queen are related.

---

### 5.4 Step 3: Positional Encoding — Word Order Matters

Transformers process all tokens simultaneously, so they don't naturally know word ORDER. Positional encoding fixes this:

```
WITHOUT POSITION:
  "Dog bites man" and "Man bites dog" look IDENTICAL
  (same words, same embeddings!)

WITH POSITION:
  "Dog"(pos=1) "bites"(pos=2) "man"(pos=3)
  "Man"(pos=1) "bites"(pos=2) "dog"(pos=3)
  Now they're DIFFERENT!
```

#### How It Works:

```
Final embedding = token_embedding + position_embedding

"cat" at position 1: [0.23, -0.41, 0.87] + [0.00, 1.00, 0.00] = [0.23, 0.59, 0.87]
"cat" at position 5: [0.23, -0.41, 0.87] + [0.96, 0.28, 0.96] = [1.19, -0.13, 1.83]

Same word, different position = different representation!
```

> Modern models (GPT-4, Llama) use **RoPE** (Rotary Position Embeddings), which handles very long sequences better than the original sinusoidal approach.

---

### 5.5 Step 4: Self-Attention — The Heart of Transformers

This is the most important concept. Self-attention lets each word look at ALL other words to understand context.

#### The Q, K, V Framework:

Every token creates three vectors:
- **Q (Query)**: "What am I looking for?"
- **K (Key)**: "What do I contain?"
- **V (Value)**: "What information do I provide?"

```
Sentence: "The cat sat on the mat"

For the word "sat":
  Q(sat) = "Who did the action? What was it about?"
  
  K(The)  = "I'm an article"           → Low match with Q(sat)
  K(cat)  = "I'm an animal/subject"    → HIGH match with Q(sat)!
  K(on)   = "I'm a preposition"        → Medium match
  K(mat)  = "I'm an object/location"   → Medium match

Attention scores (after softmax):
  sat → The:  0.02
  sat → cat:  0.65  ← "sat" pays most attention to "cat" (the subject)
  sat → sat:  0.08
  sat → on:   0.10
  sat → the:  0.02
  sat → mat:  0.13
```

#### The Math (Simplified):

```
Attention(Q, K, V) = softmax(Q × K^T / sqrt(d)) × V

1. Q × K^T         → How much should each word attend to every other word?
2. / sqrt(d)        → Scale down so numbers don't get too big
3. softmax(...)     → Convert to probabilities (sum to 1.0)
4. × V             → Weight the actual information by attention scores
```

#### A Real Example:

```
"The bank by the river was steep"
"The bank approved my loan"

For "bank" in sentence 1:
  Attention to "river" = HIGH → meaning: riverbank (nature)

For "bank" in sentence 2:
  Attention to "loan" = HIGH → meaning: financial institution

SAME WORD, different attention pattern = different meaning!
This is how transformers handle ambiguity.
```

---

### 5.6 Multi-Head Attention — Looking at Multiple Things at Once

One attention head might miss something. Solution: use MANY heads in parallel!

```
HEAD 1: Focuses on GRAMMAR
  "The cat [that I saw yesterday] sat on the mat"
  → Links "cat" to "sat" (subject-verb agreement)

HEAD 2: Focuses on MEANING
  "The cat sat on the mat"
  → Links "cat" to "mat" (the cat is ON the mat)

HEAD 3: Focuses on REFERENCE
  "The cat sat on the mat. It was soft."
  → Links "It" to "mat" (what was soft?)

HEAD 4: Focuses on POSITION
  → Tracks nearby words and sentence boundaries
```

```
GPT-4 scale:
  96 layers × 96 attention heads per layer = 9,216 attention heads!
  Each one learns to focus on different patterns.
```

---

### 5.7 Step 5: Feed-Forward Network — Thinking Time

After attention gathers relevant info, the feed-forward network PROCESSES it:

```
ATTENTION:    "I've gathered context from all relevant words"
                              ↓
FEED-FORWARD: "Now let me THINK about what this means"
                              ↓
              [Linear layer → ReLU activation → Linear layer]
                              ↓
OUTPUT:       "Here's my updated understanding of this position"
```

```
This is where the model's "knowledge" lives:
  - Facts: "Paris is the capital of France"
  - Patterns: "After 'the', a noun usually follows"
  - Reasoning: "If A > B and B > C, then A > C"
```

> Each transformer layer has BOTH attention AND feed-forward. They alternate: attend → process → attend → process × 96 layers.

---

### 5.8 Layer Normalization & Residual Connections

Two techniques that make deep networks actually trainable:

#### Residual Connections (Skip Connections):
```
Instead of: input → attention → output
Do:         input → attention → output + input  (add the original back!)

Why? If the attention layer learns nothing useful, the input
still passes through unchanged. This prevents information loss
in very deep networks (96+ layers).
```

#### Layer Normalization:
```
After each sub-layer, normalize the numbers so they don't
explode to millions or shrink to zero.

Without LayerNorm:  Layer 1: [0.5, 0.3]  → Layer 50: [1,000,000, 500,000]
With LayerNorm:     Layer 1: [0.5, 0.3]  → Layer 50: [0.7, 0.4]  (stable!)
```

---

### 5.9 The Full Transformer Block

Now let's see one complete layer:

```
┌─────────────────────────────────────────┐
│          TRANSFORMER BLOCK (×96)        │
│                                         │
│  Input                                  │
│    ↓                                    │
│  Layer Norm                             │
│    ↓                                    │
│  Multi-Head Self-Attention              │
│    ↓                                    │
│  + Residual Connection (add input)      │
│    ↓                                    │
│  Layer Norm                             │
│    ↓                                    │
│  Feed-Forward Network                   │
│    ↓                                    │
│  + Residual Connection (add input)      │
│    ↓                                    │
│  Output → (goes to next block)          │
│                                         │
└─────────────────────────────────────────┘
```

Repeat this 96 times (for GPT-4 scale) and you have the full model!

---

### 5.10 The Training Process — How LLMs Learn

#### Phase 1: Pre-training (Months, Millions of $$$)

```
GOAL: Learn language patterns from the entire internet.

DATA:    Books, Wikipedia, websites, code, forums (~13 trillion tokens)
METHOD:  "Predict the next word" — billions of times

Input:   "The Eiffel Tower is located in ___"
Target:  "Paris"
Loss:    Model predicted "London" → wrong → adjust weights slightly
         
Repeat this 13,000,000,000,000 times.
Cost:    ~$100 million+ in compute for frontier models
```

#### Phase 2: Fine-tuning / Instruction Tuning

```
GOAL: Make the model follow instructions (not just predict text).

PRE-TRAINED MODEL:
  Input: "Write a poem about AI"
  Output: "Write a poem about dogs. Write a poem about cats." (just predicts text)

AFTER FINE-TUNING:
  Input: "Write a poem about AI"
  Output: "Silicon minds awaken, digital dreams take flight..." (follows instruction!)

DATA: ~100K examples of (instruction, ideal_response) pairs
      Written by human annotators
```

#### Phase 3: RLHF / DPO — Learning Human Preferences

```
RLHF = Reinforcement Learning from Human Feedback

STEP 1: Generate 2 responses to the same prompt
  Response A: "The answer is 42. Here's why..."  
  Response B: "idk lol maybe 42?"

STEP 2: Human rates: A is better than B

STEP 3: Train the model to prefer A-style responses

This is why ChatGPT sounds helpful, polite, and structured
instead of chaotic internet text.
```

#### DPO (Direct Preference Optimization) — The Newer Approach:
```
Same goal as RLHF but simpler:
- Skip the reward model
- Directly optimize on preference pairs
- Used by Llama 3, Claude, and newer models
```

---

### 5.11 Key Takeaways — Day 5 Cheat Sheet

```
THE TRANSFORMER PIPELINE:
  Text → Tokenize → Embed → Add Position → 
  [Attention + Feed-Forward] × 96 layers → 
  Predict Next Token

ATTENTION:
  Each word asks "which other words matter for understanding me?"
  Uses Query, Key, Value matrices
  Multi-head = looks at multiple patterns simultaneously

WHY THIS MATTERS FOR AGENTS:
  - LLMs can't count letters (tokenization blind spot) → USE TOOLS
  - LLMs struggle with long sequences → MANAGE CONTEXT WINDOW
  - Temperature affects word selection → SET IT RIGHT FOR THE TASK
  - Attention = how models resolve ambiguity → WRITE CLEAR PROMPTS

TRAINING PIPELINE:
  Pre-train (predict next word on internet data)
  → Fine-tune (follow instructions)
  → RLHF/DPO (match human preferences)
```

---

## ⏱️ Part 2: Daily Lab Task (30 minutes)

### Lab: "Explore the Transformer in Action"

**Objective**: Write Python scripts that demonstrate tokenization, token counting, and model behavior differences to solidify your understanding.

### Task 1: Tokenizer Exploration
```python
# Install: pip install tiktoken
# Use tiktoken (OpenAI's tokenizer) to explore tokenization
#
# Tokenize these strings and compare:
#   1. "Hello world"
#   2. "Supercalifragilisticexpialidocious"
#   3. "12345678" (numbers)
#   4. "こんにちは" (Japanese — non-English)
#   5. "def hello_world(): print('hi')" (code)
#
# For each, print: text, tokens, token count, tokens-per-character ratio
```

### Task 2: The Strawberry Test
```python
# Ask an LLM: "How many times does the letter 'r' appear in 'strawberry'?"
# Then verify with Python: "strawberry".count("r")
#
# This demonstrates WHY agents need tools:
# The LLM sees ['str', 'aw', 'berry'] — it can't see individual letters!
#
# Build a function that:
#   1. Asks the LLM the question
#   2. Counts with Python
#   3. Compares the two answers
#   4. Prints whether the LLM was right or wrong
```

### Task 3: Temperature Experiment
```python
# Call an LLM API 5 times with the SAME prompt but different temperatures
# Prompt: "Complete this sentence: The meaning of life is"
#
# Temperatures: [0.0, 0.3, 0.7, 1.0, 1.5]
#
# For each response, print:
#   - Temperature value
#   - The response
#   - Length of response (in words)
#
# Observe: At temp=0, you should get the SAME response every time.
# At temp=1.5, responses should be wildly different.
```

### Task 4: Context Window Awareness
```python
# Build a script that:
#   1. Starts with a system prompt (count those tokens)
#   2. Adds messages to conversation history
#   3. After each message, calculates:
#      - Tokens used so far
#      - Tokens remaining (out of 128K)
#      - Percentage of context used
#   4. Prints a "context window meter" like:
#      [████████░░░░░░░░░░░░] 40% used (51,200 / 128,000 tokens)
```

### Task 5: Model Comparison
```python
# If you have access to multiple models (e.g., Groq has llama, mixtral):
# Ask the SAME question to 2 different models:
#   "Explain recursion in one paragraph."
#
# Compare:
#   - Response quality
#   - Token usage (prompt + completion)
#   - Response time
#
# This teaches you to pick the RIGHT model for the RIGHT task
# (which is a critical agent-building skill).
```

---

### Completion Checklist

- [ ] Task 1: Explored tokenization with tiktoken
- [ ] Task 2: Tested the strawberry problem (LLM vs Python)
- [ ] Task 3: Compared responses across 5 temperatures
- [ ] Task 4: Built a context window meter
- [ ] Task 5: Compared 2 different models
- [ ] Updated my_progress.json to Day 5
- [ ] Pushed day5_lab.py to GitHub

---

### Coming Tomorrow — Day 6

**LLM Providers & Ecosystem** — OpenAI vs Google vs Anthropic vs Open Source. API pricing, rate limits, model selection strategy, and when to use which model. You'll learn to pick the perfect model for every agent task.

---

> *"You don't need to build the engine to drive the car. But understanding the engine makes you a much better driver."* 🏎️
> Explore tokenization and temperature — see the transformer's behavior for yourself!
