import streamlit as st
import pandas as pd
import time
import base64

git_logo_url = "assets/github-mark.png"
linkedin = "assets/linkedin.png"
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert image to Base64

git = get_base64_image(git_logo_url)
linkedin = get_base64_image(linkedin)
st.title("Authors")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("Entwan",anchor=False)
        st.write("Final year AI student.")
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
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container(border=True):
        st.subheader("Muneef", anchor=False)
        st.write("Final year AI student.")
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
            </div>
            """,
            unsafe_allow_html=True
        )