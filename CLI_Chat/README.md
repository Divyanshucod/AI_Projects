# Local Mistral Playground

A small Python application for running and interacting with a local Mistral 7B model through Ollama.

The project was built to understand the fundamentals of LLM inference and application-level interaction.

## Architecture

```text
Python Application
        |
        v
    LLMClient
        |
        v
   Ollama HTTP API
        |
        v
     Mistral 7B
        |
        v
   Generated Response
        |
        v
    Python Application
```

## Features

* Local Mistral 7B inference using Ollama
* Chat-based conversations with message history
* System prompts and role-based messages
* Temperature and top-p generation controls
* Streaming responses
* Reusable `LLMClient` abstraction
* Basic error handling
* Basic inference observability

  * Model
  * Input tokens
  * Output tokens
  * Latency

## Project Structure

```text
CLI_Chat/
├── experiments/
│   ├── basic-chat.py
│   ├── conversation.py
│   ├── client.py
│   ├── testing.py
└── README.md
```

## Requirements

* Python 3.14.6
* Ollama
* Mistral 7B model

Install and run Mistral:

```bash
ollama pull mistral:7b
ollama run mistral:7b
```
## Usage

The main interaction with the model is handled through `LLMClient`.

```python
from Client import llmClient


client = llmClient()
messages = [
    {'role':'user',
    'content':"Hi!"}
]


print(client.chat(messages))
```

Streaming:

```python
for chunk in client.steam(messages):
    print(chunk, end="", flush=True)
```

## What I Learned

Key concepts explored:

* LLM inference
* Tokens and model context
* Chat messages and roles
* System prompts
* Temperature
* Top-p sampling
* Streaming generation
* HTTP APIs
* Conversation state
* Error handling
* LLM client abstraction
* Basic inference observability