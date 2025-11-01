import streamlit as st

st.title("Magic App")

if st.button("Magic button"):
    st.success("Your name is shantanu")


guess = st.checkbox("Guess age")

if guess:
    st.write("Your age is 20")


powers = st.radio("choose your super Hero:", ["Superman", "Flash", "Ironman",
                                               "Spider-man", "Captain America", "Thor"])

st.write(f"You are {powers}")

persona = st.selectbox("Select your favourite book:", ["The Shallows", "Bhagvat Gita", "Mindset", "Deep-Work"
"Graphs", "Atomic Habbits"])

st.write(f"you selected {persona}, which is a very excellent book")

mood = st.slider("Your mood today:", 0,10,5)


num = st.number_input("how many powers you want to hold:", min_value=1, max_value=10, step=1)
st.write(f"Selected number of powers {num}")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello {name}, welcome to magic app.")


dob = st.date_input("Enter your birth date:")
if dob:
    st.write(f"Date of birth of {name} is {dob}")