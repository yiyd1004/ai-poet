import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title("AI Poet")
content = st.text_input("Please enter subject")

if st.button("Start"):
    with st.spinner("Please wait......"):
        result = llm.predict(
            "Write a poem of " + content + " within 3 sentences")
        print(result)
        st.write(result)
