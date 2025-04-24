import streamlit as st
import pandas as pd
import time
import base64

git_logo_url = "assets/github-mark.png"
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert image to Base64

git = get_base64_image(git_logo_url)

st.title("Authors")
st.title("Authors")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Entwan")
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; text-align: center; margin-top: 10px;">
                <a href="https://github.com/Enkhamgalan1230" target="_blank" style="text-decoration: none;">
                    <img src="data:image/png;base64,{git}" 
                         alt="github" 
                         style="width: 50px; height: 50px; cursor: pointer; transition: transform 0.3s ease-in-out;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container(border=True):
        st.subheader("Muneef")
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; text-align: center; margin-top: 10px;">
                <a href="https://github.com/MuneefMumthas" target="_blank" style="text-decoration: none;">
                    <img src="data:image/png;base64,{git}" 
                         alt="github" 
                         style="width: 50px; height: 50px; cursor: pointer; transition: transform 0.3s ease-in-out;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )