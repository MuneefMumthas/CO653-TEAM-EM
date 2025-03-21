import streamlit as st
import pandas as pd
import time
import base64


st.set_page_config(
    page_title="LoanEM",  # Set the title in the navigation bar
    page_icon="🏦",  # Set a custom icon (optional)
    layout="wide"  # Optionally, set layout to 'wide' or 'centered'
)

# Page Setup

home_page = st.Page(
    page = "pages/page1.py",
    title= "Home Page",
    icon = "🏠"
)

nn = st.Page(
    page = "pages/page2.py",
    title= "Neural Network",
    icon = "🧠"
)

fuzzy = st.Page(
    page = "pages/page3.py",
    title= "Fuzzy Logic",
    icon = "📝"
)

outcome = st.Page(
    page = "pages/page4.py",
    title= "Outcome",
    icon = "🏷️"
)



pg = st.navigation(
    {
        "Info": [home_page],
        "Main Logics":[nn,fuzzy],
        "Boring Stuff": [outcome]
    }
)



#st.logo("assets/logo_longer_white.png",icon_image="assets/logo.png", size= "large")

pg.run()
