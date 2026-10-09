# Agentic AI Projects 🚀

A hands-on Agentic AI learning project built with Python, LLMs, tools, conversation memory, guardrails, internet search, and human-in-the-loop (HITL) approval.

This repository contains three projects that demonstrate how to build AI applications, integrate external tools, maintain conversational context, and implement controlled agent actions.

## 📌 Projects

### 1. AI Chatbot Agent

An interactive AI chatbot powered by Groq and an LLM. The agent can respond to user queries, use tools, and search the internet for relevant information.

**Features**

* LLM-powered conversational AI.
* Conversation memory to maintain context.
* Internet search using Tavily.
* Custom tool calling.
* A greeting tool that demonstrates how agents execute tools.
* Interactive command-line interface.

**Technologies:** Python, AgentSpan, Groq, Tavily, python-dotenv.

### 2. Customer Support Agent

An AI customer support agent that retrieves order information and supports a controlled refund workflow.

**Features**

* Structured responses using Pydantic.
* Order lookup through a custom database tool.
* Refund processing tool requiring human approval.
* Input guardrails to block selected prompt-injection phrases.
* Conversation memory.
* Streaming agent events and approval handling.

**Human-in-the-Loop workflow**

1. The user asks about an order or requests a refund.
2. The agent uses its tools to retrieve order details.
3. If a refund action requires approval, the agent waits for a human decision.
4. The human approves or rejects the action.
5. The agent returns a structured response.

> Note: The current implementation uses mock order data. It is a learning project, not a production payment or refund system.

### 3. Groq LLM CLI

A simple command-line AI application using the Groq Python SDK.

**Features**

* Direct LLM API calls.
* Environment-variable-based API key configuration.
* Interactive question-and-answer loop.
* Concise responses using system instructions.

## 🧠 Agentic AI Concepts Practiced

* AI agents and LLM integration
* Tool calling and custom tools
* Conversation memory
* Internet search integration
* Input guardrails
* Structured outputs with Pydantic
* Human-in-the-Loop approval
* Agent runtime and event streaming
* Environment variables and API key management

## 🛠️ Tech Stack

* **Language:** Python
* **Agent Framework:** AgentSpan
* **LLM Providers:** Groq and OpenAI-compatible model configurations
* **Internet Search:** Tavily
* **Data Validation:** Pydantic
* **Environment Management:** python-dotenv
* **Dependency Management:** uv

## 📂 Project Structure

```text
Agentic-AI/
├── chatbot_agent.py
├── customer_support.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── README.md
└── .env                 # Local only; not committed
```

## ⚙️ Getting Started

### Prerequisites

* Python version compatible with the project dependencies.
* [uv](https://docs.astral.sh/uv/) installed.
* API keys for the providers and tools used by the selected project.

### 1. Clone the repository

```bash
git clone https://github.com/mysstudy194/Agentic-Ai.git
cd Agentic-Ai
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root directory.

Add the keys required by the project you want to run:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholders with your own API keys. Never commit your `.env` file or expose secret keys publicly.

### 4. Run the applications

**Groq LLM CLI**

```bash
uv run main.py
```

**Chatbot Agent**

```bash
uv run chatbot_agent.py
```

**Customer Support Agent**

```bash
uv run customer_support.py
```

Enter `q` to exit the interactive loops where supported.

> Run each application according to its configured provider and dependencies. The customer support agent is configured with an OpenAI model, while the chatbot agent uses a Groq model.

## 🔐 Security Notes

* API keys should be stored in `.env` and excluded from version control.
* Input guardrails provide a basic demonstration and are not a complete defense against prompt injection.
* Human approval should be enforced for sensitive operations.
* The current order database and refund operation are simulated and must not be used for real transactions.

## 🎯 Project Goal

The goal of this repository is to learn Agentic AI by building practical applications and experimenting with agents, tools, memory, guardrails, external APIs, and human approval workflows.

This project will continue to evolve as more Agentic AI concepts and real-world use cases are implemented.

## 👨‍💻 Author

**Talha Abid**

GitHub: [@mysstudy194](https://github.com/mysstudy194)
