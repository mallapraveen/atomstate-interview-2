import os

import streamlit as st
from qa_pdf import query, load_pdf

st.title("Atomstate Interview Question PDF Retrieval")

st.write("# PDF Retrieval")


uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    with open("./src/temp.pdf", "wb") as file:
        file.write(bytes_data)

    retriever = load_pdf("./src/temp.pdf")

q = st.text_input("Enter the query")

if st.button("Submit"):
    result = query(retriever, q)
    st.write(f"# Answer : {result}")
