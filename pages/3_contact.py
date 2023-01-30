import streamlit as st
from streamlit_lottie import st_lottie
from main import load_lottieurl, SOCIAL_MEDIA
import webbrowser
#import webbrowser


st.title("Contact")

lottie_media = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_osdxlbqq.json")

st_lottie(lottie_media, height=300, key="coding")

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
        