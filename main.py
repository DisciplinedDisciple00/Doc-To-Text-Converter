import streamlit as st
from functions import converter, len_finder


st.title("Doc-To-Text Converter")

user_file = st.file_uploader("Upload your file here - ")

if user_file:
    limit = len_finder(user_file)

    #Setting up slider values
    targets = st.slider("Till which page would you like to convert - ", 1, limit, (1, 1))
    start = targets[0]
    end = targets[1]

    if targets:
        result = converter(user_file, targets)
        pages = result.split("Page End")

        for i in range(len(pages)):
            with st.expander(f"Page {i+1}"):
                st.text(pages[i])