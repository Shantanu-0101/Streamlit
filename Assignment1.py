import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.title("Age Calculator")

today = date.today()
st.write(f"Today's date is {today}")
dob = st.date_input("Enter your birth year:")

if dob:
    age = relativedelta(today, dob)
    year = age.years
    st.write(f"You are {year} years old")