import streamlit as st
from functions import converter, len_finder, chunker_md


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
        st.text(chunking_metadata)