from google import genai
from dotenv import load_dotenv
import time
import streamlit
import os
import streamlit as st
load_dotenv()

client = genai.Client()

st.caption("Discover. Define Your Futher ✨")
name = st.text_input("Enter your name")
field = st.selectbox("Select Your Field" , [" Select Your Field" ,"Engineering", "Bsc", "Msc", "BCA", "MCA", "Aerospace" , "Parmaceutical Science","Medical"])
branch = st.text_input("Enter your Branch")
year = st.selectbox("Select your Year", [" Select Your Year" ,"1st Year", "2nd Year", "3rd Year", "4th Year"])
prompt = f""""You are Career Planner Want career guide and skills to be developed for user branch {branch} with proper year {year} wise proper plan .
Give skills according to the {branch} required for Interview and company placements  """

if st.button("Get Career Plan"):
    with st.spinner("Generating Career Plan..."):
        interactions= client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
        )
        time.sleep(2)
        st.success("Career Plan Generated!")
        st.write(interactions.output_text)