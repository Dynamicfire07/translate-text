from backend import translate, converstion
import streamlit as st

st.title("Translate Your Queries")

column1, column2 = st.columns(2)
with column1:
    language1 = st.selectbox("Select language", options=[
        "English",
        "Spanish",
        "French",
        "German",
        "Chinese",
        "Japanese",
        "Russian",
        "Arabic",
        "Portuguese",
        "Hindi",
        "Bengali",
        "Korean",
        "Italian",
        "Dutch",
        "Turkish",
        "Swedish",
        "Polish",
        "Vietnamese",
        "Thai",
        "Indonesian"
    ]
                             )
    input = st.text_area("Enter Text to be translated",key="1")


with column2:
    language2 = st.selectbox("Select language 2", options=[
        "English",
        "Spanish",
        "French",
        "German",
        "Chinese",
        "Japanese",
        "Russian",
        "Arabic",
        "Portuguese",
        "Hindi",
        "Bengali",
        "Korean",
        "Italian",
        "Dutch",
        "Turkish",
        "Swedish",
        "Polish",
        "Vietnamese",
        "Thai",
        "Indonesian"
    ])

    lang1,lang2 = converstion(input_lang=language1,output_lang=language2)


