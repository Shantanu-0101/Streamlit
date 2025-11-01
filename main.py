import streamlit as st

st.title("👋 Hello, Streamlit!")
st.write("If you can see this, your setup works perfectly 😄")

name = st.text_input("Enter your name:")
if st.button("Say Hi"):
    st.success(f"Hello {name}, welcome to Streamlit!")
