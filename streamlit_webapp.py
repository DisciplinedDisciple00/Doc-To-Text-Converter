import streamlit as st
import requests as req
from backend.services.functions import len_finder

st.title("Pdf-To-Text Converter")

user_file = st.file_uploader("Upload your file here - ")

if user_file:
    limit = len_finder(user_file)

    #Setting up slider values
    targets = st.slider("Till which page would you like to convert - ", 1, limit, (1, limit))
    start = targets[0]
    end = targets[1]

    if targets:
        #Api connection for RAG
        text_response = req.post(
            "http://127.0.0.1:8000/upload",
            files={
                "file": (
                    user_file.name,
                    user_file.getvalue(),
                    "application/pdf"
                )
            },
            data={
                "start": start,
                "end": end
            }
        )
        result = text_response.json()

        for i in range(len(result)):
            with st.expander(f"Page {i+1}"):
                st.text(result[i])

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display previous messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        query = st.chat_input("Enter your query...")

        if query:
            # Display user message
            with st.chat_message("user"):
                st.markdown(query)

            # Store user message
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": query
                }
            )

            # Call backend
            with st.spinner("Thinking..."):
                api_response = req.post(
                    url="http://127.0.0.1:8000/chat",
                    json={"message": query}
                )

                response = api_response.json()["answer"]

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)

            # Store assistant response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )