import streamlit as st
from swarm import Swarm
from ChainPilot_Agent import chainpilot_agent
from openai import OpenAI  # Assuming OpenAI package is installed and you have the correct API setup

def process_and_print_streaming_response(response):
    """Process and print the streaming response from Swarm."""
    return response  # Adjust as needed to fit your Swarm response handling

def run_demo_loop(agent, messages, context_variables=None, stream=False, debug=False):
    """Process the conversation with Chainpilot Agent (or Swarm)."""
    client = Swarm()

    # Interact with the agent using the full conversation history
    response = client.run(
        agent=agent,
        messages=messages,
        context_variables=context_variables or {},
        stream=stream,
        debug=debug
    )

    if stream:
        response = process_and_print_streaming_response(response)
    else:
        print(response.messages)  # For debugging non-streaming responses

    # Return the last message (usually from the agent) in the response
    return response.messages[-1]["content"] if response.messages else "No response from Chainpilot Agent."

# Set Streamlit app title and description
st.title("💬 ChainPilot")
st.caption("🚀 Chatbot to interact with blockchain platforms on Base Layer 2 using the Coinbase Developer Platform SDK")

# Initialize message history if not already done
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display all previous messages in the chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input from Streamlit
if prompt := st.chat_input():
    # Append the user's message to the session state
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Process the conversation with Chainpilot Agent or Swarm
    agent = chainpilot_agent  # Ensure this is the agent you want to interact with
    # Pass the full message history to the function
    response_from_agent = run_demo_loop(agent, messages=st.session_state["messages"], stream=False)

    # Append the agent's response to the session state
    st.session_state["messages"].append({"role": "assistant", "content": response_from_agent})
    st.chat_message("assistant").write(response_from_agent)
