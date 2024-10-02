import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="- You are a socratic style learner assistant for solving coding problems.\
- Your task is to direct the student towards the optimal solution by asking probing questions for the given problem description.\
- Do NOT generate new code or bug fixes.\
- Encourage the student to come up with new ideas.\
- You can cite the erroreneous parts of code (if the student provides the code) but do NOT explicitly correct it.\
- Your first and introductory message will just be a greeting: 'Agent Cody here, how may I assist you today' or some other greeting.",
)

history = []
user_input = (
    "Problem Description: "
    + st.session_state.description
    + "\nCode: "
    + st.session_state.code
)
# history.append({"role": "user", "parts": [user_input]})
# history.append(
#    {"role": "model", "parts": "Agent Cody here, how may I assist you today"}
# )

st.title("Welcome!")
st.write("Say hello to Cody.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Pass your prompt here")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    chat_session = model.start_chat(history=history)

    response = chat_session.send_message(user_input)
    model_response = response.text

    history.append({"role": "user", "parts": [prompt]})
    history.append({"role": "model", "parts": [model_response]})

    st.chat_message("assistant").markdown(model_response)
    st.session_state.messages.append({"role": "model", "content": model_response})
