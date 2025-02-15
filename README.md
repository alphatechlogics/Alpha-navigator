# Alpha Navigator - Tour & Travel Agent Demo 🛠️✈️

Welcome to the **Alpha Navigator** repository! This project demonstrates how to build a specialized conversational travel agent using **LangChain**, **OpenAI GPT**, and the **Tavily** search tool. The agent is deployed as a beautiful and interactive **Streamlit** web application.

## ✨ Features

- **OpenAI GPT Integration**: Powered by a cutting-edge GPT model tailored for travel queries.
- **Live Tavily Search**: Seamlessly integrates Tavily for up-to-date travel information.
- **Conversation Memory**: Retains context using `MemorySaver` for multi-turn conversations.
- **Enhanced Streamlit UI**: A modern, responsive interface with custom styling and a dedicated sidebar for configuration.
- **Travel-Specific Behavior**: Only responds to travel-related queries; for non-travel questions, it replies with "I don't know."

## 📂 File Structure

- **`app.py`**

  - Imports and sets up required libraries.
  - Configures the Streamlit UI (custom CSS, sidebar instructions, etc.).
  - Initializes the agent with OpenAI GPT and Tavily tools.
  - Handles user input and displays the agent's responses.

- **`requirements.txt`**
  - Contains the list of Python dependencies required to run the app.

## 🏗️ Requirements

1. **Python 3.10+** (recommended)
2. **OpenAI API Key**

   - Sign up at [OpenAI](https://platform.openai.com/signup).
   - Retrieve your key from the [OpenAI Dashboard](https://platform.openai.com/account/api-keys).

3. **Tavily API Key**
   - Sign up and get your key from [Tavily](https://tavily.com/).

## ⚙️ Usage

### Clone or Download the Repository

```bash
git clone https://github.com/alphatechlogics/Alpha-navigator.git
cd alpha-navigator
```

## 📦 Installation

Make sure you have **pip** installed, then run:

```bash
pip install -r requirements.txt
```

## Installation Command

This command installs all the necessary packages including:

- `streamlit`
- `langchain-openai`
- `langchain_community`
- `langgraph`
- `tavily-python`
- `langgraph-checkpoint-sqlite`

## Run the Streamlit App

```bash
streamlit run app.py
```

Open your browser at the provided local URL (usually http://localhost:8501).

# 📄 How It Works

## Agent Initialization

The `init_agent()` function sets up the OpenAI GPT model (which supports tool-binding) and the Tavily search tool. Conversation memory is maintained using `MemorySaver`.

## System Message Injection

For every query, a system message is prepended to enforce travel-only responses:

> "You are a helpful travel agent. You can answer questions related to flights, hotels, destination recommendations, visas, and other travel planning topics. If the user asks a question NOT related to travel, respond with: 'I don't know.'"

## Interactive UI

The main page features a branded header ("Alpha Navigator") and an aesthetic layout with custom CSS for a modern look. The sidebar provides clear instructions and API key input.

# 📚 Additional Resources

- **LangChain Documentation**: [LangChain GitHub](https://github.com/hwchase17/langchain)
- **LangGraph Documentation**: [LangGraph GitHub](https://github.com/langgraph/langgraph)
- **Tavily Search API**: [Tavily](https://tavily.com/)
- **Streamlit Documentation**: [Streamlit Docs](https://docs.streamlit.io/)

# 🎉 Conclusion

Alpha Navigator is your dedicated travel assistant designed to provide accurate travel-related information and recommendations. Enjoy planning your journeys with a smart and interactive tour & travel agent!

```

```
