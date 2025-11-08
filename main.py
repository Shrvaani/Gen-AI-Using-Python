# app.py (Streamlit version using Hugging Face GPT-OSS)
import os
from colorama import Fore
from dotenv import load_dotenv
import streamlit as st
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = "openai/gpt-oss-20b"

# Initialize Hugging Face client
if not HF_TOKEN:
    st.error("⚠️ Missing HF_TOKEN in your .env file")
    st.stop()

llm_client = InferenceClient(model=MODEL, token=HF_TOKEN)

# Function to query the Hugging Face model
def ask_model(prompt: str) -> str:
    try:
        response = llm_client.chat_completion(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=400,
            temperature=0.7,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error communicating with model: {e}"

# Streamlit UI — same logical flow, just web-based
st.set_page_config(page_title="Hugging Face GPT-OSS Assistant", layout="centered")

st.title("🧠 GPT-OSS Streamlit Assistant")
st.markdown("Type your question below. Click **Submit** to get an answer.")

# Simulate your “MENU” logic in a simple Streamlit interface
choice = st.radio("Select an option:", ["Ask a question", "Exit"])

if choice == "Ask a question":
    user_input = st.text_input("Q:", placeholder="Type your question here...")
    if user_input:
        st.write(Fore.YELLOW + "Thinking..." + Fore.RESET)
        answer = ask_model(user_input)
        st.markdown(f"**A:** {answer}")

elif choice == "Exit":
    st.info("👋 Session ended. Close the app window to exit.")
