from google import genai
from dotenv import load_dotenv
import time
import streamlit
import os
import streamlit as st
load_dotenv()

client = genai.Client()

import streamlit as st

st.set_page_config(
    page_title="Career Sarthi",
    page_icon="🎓",
    layout="wide"
)

# Background colour and website styling
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #475569,
        #64748B,
        #6B7280
    );
}
/* Website Name */
.website-title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    color: #ffffff;
    padding-top: 30px;
    letter-spacing: 2px;
}

/* Tagline */
.website-subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 5px;
}

/* Sidebar Background */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Text Colour */
h1, h2, h3, p, label {
    color: white !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #6366f1,
        #06b6d4
    );
    color: white;
    border-radius: 10px;
    border: none;
}

/* Footer */
.footer {
    text-align: center;
    color: #cbd5e1;
    padding: 20px;
}

</style>

<div class="website-title">
    🎓 CAREER SARTHI
</div>

<div class="website-subtitle">
    Your Guide Towards a Bright Future
    Discover. Define Your Future ✨
</div>

""", unsafe_allow_html=True)



name = st.text_input("Enter your name")
field = st.selectbox("Select Your Field" , [" Select Your Field" ,"Engineering", "Bsc", "Msc", "BCA", "MCA", "Aerospace" , "Parmaceutical Science","Medical"])
branch = st.text_input("Enter your Branch")
year = st.selectbox("Select your Year", [" Select Your Year" ,"1st Year", "2nd Year", "3rd Year", "4th Year"])
prompt = f""""You are Career Planner Want career guide and skills to be developed for user branch {branch} with proper year {year} wise proper plan .
Give skills according to the {branch} required for Interview and company placements {branch}{year}{field}  provide plan for entier rest year ex. If user is in 1year then provide plan for 1,2,3,4 years and if user is in 2year then provide for 2,3,4 years plan 
use little bright color in the plan"""

if st.button("Get Career Plan"):
    with st.spinner("Generating Career Plan..."):
        interactions= client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
        )
        time.sleep(2)
        st.success("Career Plan Generated!")
        st.write(interactions.output_text)