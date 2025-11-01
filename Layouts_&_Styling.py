import streamlit as st


st.title("Poll for Powers")

col1, col2 = st.columns(2)

with col1:
    st.header("Spider-Man")
    st.image("https://images.pexels.com/photos/5691158/pexels-photo-5691158.jpeg", width=100)
    vote1 = st.button("Vote Spidey")

with col2:
    st.header("Flash")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCl2niAuomKBb-Tefr1pzefCRTBpdwpvE4Ng&s", width=200)
    vote2 = st.button("Vote The Speed")

if vote1:
    st.success("With Great Powers We get Great Responsibilities")

elif vote2:
    st.success("I'm the fastest Man alive")


name = st.sidebar.text_input("Enter your name:")
theme = st.sidebar.selectbox("Choose Your Theme:", ["Dark black", "Brownie", "Light"])

st.write(f"Welcome {name}, Your Theme is {theme}")


with st.expander("Show Super power gaining strategy"):
    st.write(""" 
    1. Work Hard
    2. Control your thoughts
    3. Earn money
""")
    

st.markdown('# Welcome to freedom')
st.markdown('> Stay positive at any cost')