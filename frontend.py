import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Dental Appointment Assistant",
    page_icon="🦷",
    layout="centered"
)

st.title("🦷 Dental Appointment Assistant")
st.write("Ask about appointments, booking, cancellation, or rescheduling.")

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
if prompt := st.chat_input("Type your message..."):

    # show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # send request to FastAPI
    try:
        response = requests.post(
            API_URL,
            json={"message": prompt}
        )

        data = response.json()
        bot_reply = data["response"]

    except Exception as e:
        bot_reply = "⚠️ Error connecting to FastAPI server."

    # show assistant message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })
