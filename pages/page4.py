import streamlit as st
import pandas as pd
import time
import base64

git_logo_url = "assets/github-mark.png"
linkedin = "assets/linkedin.png"
email = "assets/email.png"
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Converting image to Base64
git = get_base64_image(git_logo_url)
linkedin = get_base64_image(linkedin)
email = get_base64_image(email)
st.title("Authors")

# Creating two side-by-side columns for the authors' information
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Entwan",anchor=False)
        st.write("Artificial Intelligence engineer | Data Scientist. I hate coding but mom told me to, so..")
        st.markdown(
            f"""
            <style>
                .icon-container a img {{
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }}
                .icon-container a:hover img {{
                    transform: scale(1.15);
                    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
                }}
            </style>

            <div class="icon-container" style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 10px;">
                <a href="https://github.com/Enkhamgalan1230" target="_blank">
                    <img src="data:image/png;base64,{git}" 
                        alt="GitHub" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
                <a href="https://www.linkedin.com/in/entwan/" target="_blank">
                    <img src="data:image/png;base64,{linkedin}" 
                        alt="LinkedIn" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
                <a href="mailto:enkhamgalan.entwan@outlook.com">
                    <img src="data:image/png;base64,{email}" 
                        alt="Email" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")

with col2:
    with st.container(border=True):
        st.subheader("Muneef", anchor=False)
        st.write("AI Student | Passionate about Integrating AI into Apps, Games & Businesses")
        st.markdown(
            f"""
            <style>
                .icon-container a img {{
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }}
                .icon-container a:hover img {{
                    transform: scale(1.15);
                    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
                }}
            </style>

            <div class="icon-container" style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 10px;">
                <a href="https://github.com/MuneefMumthas" target="_blank">
                    <img src="data:image/png;base64,{git}" 
                        alt="GitHub" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
                <a href="https://www.linkedin.com/in/muneefmumthas/?originalSubdomain=uk" target="_blank">
                    <img src="data:image/png;base64,{linkedin}" 
                        alt="LinkedIn" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
                <a href="mailto:muneef.mumthas@outlook.com">
                    <img src="data:image/png;base64,{email}" 
                        alt="Email" 
                        style="width: 50px; height: 50px; border-radius: 10px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")