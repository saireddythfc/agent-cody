import streamlit as st

st.set_page_config(
    page_title="Project Cody",
    page_icon="👋",
)

st.title("Home Page")
st.sidebar.success("Select a page above.")

if "description" not in st.session_state:
    st.session_state["description"] = ""

if "code" not in st.session_state:
    st.session_state["code"] = ""

description = st.text_area(
    "Enter the problem description", st.session_state["description"]
)

code = st.text_area("Enter the implemented solution", st.session_state["code"])
submit = st.button("Submit")
if submit:
    st.session_state["description"] = description
    # st.write("Your problem description: ", description)

    st.session_state["code"] = code
    # st.write("You implemented solution: ")
    # st.code(code, language="python")
    st.write("Thanks for submitting")
    st.write("You can now navigate to Agent Cody to solve your problems.")
