import streamlit as st


st.title("Ask a question to an image")

st.header("please upload an image")

file=st.file_uploader("",type=['jpeg','jpg','png'])

if file:
    st.image(file,use_column_width=True)
    user_question=st.text_input('Ask a question about your image:')


    if user_question and user_question != "" :
        st.write("dummy response")
