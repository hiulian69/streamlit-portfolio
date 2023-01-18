import streamlit as st
from streamlit_lottie import st_lottie
from main import load_lottieurl


PROJECTS = {
    "🏗️ Bank Chrun Prediction - Finding the most relevant features that predict Churning": "https://github.com/hiulian69/Bank_Churn_Prediction",
    "🏗️ Personal Spotify Data Dashboard in Tableau": "https://public.tableau.com/app/profile/horia.iulian.state/viz/SpotifyPersonalData_16715360463390/Dashboard2",
    "🏗️ First Personal Portfolio in streamlit":"https://github.com/hiulian69/streamlit-portfolio"
}


lottie_vibe = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_mhsbede7.json")

st_lottie(lottie_vibe, height=400, key="coding")

# --- Projects  ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



st.write("---")
st.write("To be continued...")