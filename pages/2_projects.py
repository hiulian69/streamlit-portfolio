import streamlit as st
from streamlit_lottie import st_lottie
from main import load_lottieurl, PROJECTS




lottie_vibe = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_mhsbede7.json")

st_lottie(lottie_vibe, height=400, key="coding")

# --- Projects  ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")