import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from pathlib import Path 


st.set_page_config(page_title="My Webpage", page_icon=":wave:", layout="wide")

#st.sidebar.success("Select page")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "res" / "CV_STATE.pdf"
profile_pic = current_dir / "res" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Horia- Iulian State"
PAGE_ICON = ":wave:"
NAME = "Horia-Iulian State"
DESCRIPTION = """
Data Science student eager to learn new technique.
"""
EMAIL = "horia.istate@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/horia-iulian-state-994ab7252/",
    "GitHub": "https://github.com/hiulian69/",
    "Instagram": "https://www.instagram.com/horiaiulian/",
}
PROJECTS = {
    "🏆 Bank Chrun Prediction - Finding the most relevant features that predict Churning": "https://github.com/hiulian69/Bank_Churn_Prediction",
    "🏆 Personal Spotify Data Dashboard in Tableau": "https://public.tableau.com/app/profile/horia.iulian.state/viz/SpotifyPersonalData_16715360463390/Dashboard2"
}

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iv4dsx3q.json")


# ---- HEADER SECTION ----
with st.container():
	st.subheader("Hi, there, welcome to my web portfolio.")
	st.title("Aspiring Data Analyst from Romania.")
	st.write("""You can call me Julian. Data Science student interested in gaining experience in a professional field. 
        Curious and excited about working with data and supporting taking data-driven decisions. 
      """)
# --- LOAD CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
# --- HERO SECTION ---

col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
        )
    st.write("E-mail:", EMAIL)


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who am I ")
        st.write("##")
        st.write(
            """
            Originally from Brasov, Romania. Moved to Vienna in search for new opportunities.
            After some years working different types of jobs, I fell in love with manipulating and 
            analysing data and decided to try new path in my career. 
            I am now doing my Data Science Bachelor at International University for Applied Science, Erfurt Germany. 
            Being located in Vienna, Austria and excited for new data challenges.
            """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")




# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.header("Skills, Tools & Languages")
    first_column, sec_column, thir_column, for_column = st.columns(4)

    with first_column:
        st.button("Python")
        st.button("SQL")     
        st.button("Excel")

    with sec_column:
        st.button("Tableau")
        st.button("Streamlit")     
        st.button("Scikit-learn")
   
    with thir_column:
        st.button("ML")
        st.button("R")     
        st.button("Docker")
    
    with for_column:
        st.button("German - C1")
        st.button("English - C1")     
        st.button("Romanian - Native")
 