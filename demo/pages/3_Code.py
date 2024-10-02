import streamlit as st


st.title("Source Code")

st.code(st.session_state["code"], language="python")
