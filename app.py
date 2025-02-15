import streamlit as st
import os

# Use the community wrapper, not the standard ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# Set up page configuration and custom CSS for a polished UI
st.set_page_config(
    page_title="Alpha Navigator - Tour & Travel Agent",
    page_icon="✈️",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #F8F9FA;
        color: #333;
    }
    .header {
        font-size: 3em;
        font-weight: 700;
        color: #2C3E50;
    }
    .subheader {
        font-size: 1.2em;
        color: #34495E;
    }
    .agent-response {
        background-color: #FFFFFF;
        padding: 1em;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar configuration and instructions
st.sidebar.header("API & Agent Configuration")
st.sidebar.markdown(
    """
    **Alpha Navigator** is your specific tour & travel assistant powered by OpenAI and Tavily.
    
    - Enter your **OpenAI API Key** and **Tavily API Key** below.
    - Click **Initialize Agent** to start.
    - Use the input box to ask travel-related questions (e.g. flights, hotels, destinations).
    - For non-travel questions, the agent will respond with "I don't know."
    """
)


def init_agent(openai_key: str, tavily_key: str):
    # Set the Tavily API key in the environment
    os.environ["TAVILY_API_KEY"] = tavily_key
    memory = MemorySaver()

    # Create the ChatOpenAI model (which supports .bind_tools())
    model = ChatOpenAI(
        openai_api_key=openai_key,
        model_name="gpt-4o-mini-2024-07-18",  # Change model as needed
        temperature=0.0
    )

    # Create the Tavily search tool
    search = TavilySearchResults(max_results=2)
    tools = [search]

    # Create the agent (without system_template since it is unsupported)
    agent_executor = create_react_agent(
        model,      # pass model positionally
        tools,
        checkpointer=memory
    )
    return agent_executor


def main():
    st.markdown('<div class="header">Alpha Navigator</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="subheader">Your Personal Tour & Travel Agent</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Input API keys in the main area (alternative to sidebar if desired)
    openai_api_key = st.text_input(
        "Enter your OpenAI API Key", type="password")
    tavily_api_key = st.text_input(
        "Enter your Tavily API Key", type="password")

    if "agent_executor" not in st.session_state:
        st.session_state["agent_executor"] = None

    if st.button("Initialize Agent"):
        if not openai_api_key or not tavily_api_key:
            st.error("Please provide both OpenAI and Tavily API keys.")
        else:
            st.session_state["agent_executor"] = init_agent(
                openai_key=openai_api_key,
                tavily_key=tavily_api_key
            )
            st.success("Alpha Navigator is initialized and ready!")

    st.markdown("### Ask Alpha Navigator a travel-related question")
    user_input = st.text_input("Your question:")

    if st.button("Send"):
        if not user_input.strip():
            st.warning("Please enter a question.")
            return
        if not st.session_state["agent_executor"]:
            st.error("Please initialize the agent first.")
            return

        # Prepend a system message with travel-specific instructions
        system_message = SystemMessage(content="""
You are a helpful travel agent. You can answer questions related to flights, hotels, destination recommendations, visas, and other travel planning topics.
If the user asks a question NOT related to travel, respond with: "I don't know."
        """.strip())

        # Combine the system message with the user's question
        messages = [system_message, HumanMessage(content=user_input)]

        config = {"configurable": {"thread_id": "streamlit_demo"}}
        response = st.session_state["agent_executor"].invoke(
            {"messages": messages},
            config=config
        )
        messages_response = response.get("messages", [])
        if not messages_response:
            st.markdown(
                '<div class="agent-response">**Assistant:** (No messages in response)</div>', unsafe_allow_html=True)
            return

        last_message = messages_response[-1]
        if hasattr(last_message, "content"):
            st.markdown(
                f'<div class="agent-response"><strong>Assistant:</strong> {last_message.content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="agent-response"><strong>Assistant:</strong> (No content in final message)</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
