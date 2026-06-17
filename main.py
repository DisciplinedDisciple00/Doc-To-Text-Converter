import streamlit as st
from functions import converter, len_finder, chunker_md
from rag import embedder, chunker, store, query_embedder, retrieve
from llm import prompt_builder, response


st.title("Pdf-To-Text Converter")

user_file = st.file_uploader("Upload your file here - ")

if user_file:
    limit = len_finder(user_file)

    #Setting up slider values
    targets = st.slider("Till which page would you like to convert - ", 1, limit, (1, 1))
    start = targets[0]
    end = targets[1]

    if targets:
        result = converter(user_file, targets)

        for i in range(len(result)):
            with st.expander(f"Page {i+1}"):
                st.text(result[i])

        chunking_metadata = chunker_md(result)
        chunking_data = chunker(chunking_metadata)
        embeddings = embedder(chunking_data)

        store(chunking_data, embeddings)

        query = st.chat_input("Enter your query : ")
        if query:
            query_embeddings = query_embedder(query)
            retrieved_data = retrieve(query_embeddings)

            prompt = prompt_builder(query, retrieved_data)

            response = response(prompt)

            with st.expander("Response"):
                st.text(f"{response}")