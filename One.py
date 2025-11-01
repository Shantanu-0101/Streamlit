import streamlit as st


st.title("Hello Shantanu")
st.subheader("Welcome to streamlit app")
st.text("Your first interactive app")
st.write("We love code.")

box = st.selectbox("Your fav language:", ["python", "Javascript", "Rust", "Solidity", "Basic"])
st.write(f"You choose:  {box}, which is an excellent choice")

st.success("Brewed by streamlit")