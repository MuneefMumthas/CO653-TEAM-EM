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
    title= "Project Overview",
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

fuzz2 = st.Page(
    page = "pages/fuzzy.py",
    title= "Fuzzy Logic",
    icon = "📝"
)



pg = st.navigation(
    {
        "Info": [home_page],
        "Models":[nn,fuzzy],
        "Comparison": [outcome]
    }
)

st.sidebar.header("Team Members")
st.sidebar.write("- **Enkh-Amgalan Enkhbayar (22135347)**")
st.sidebar.write("- **Muneef Ahamed Mohamed Mumthas (22206529)**")


#st.logo("assets/logo_longer_white.png",icon_image="assets/logo.png", size= "large")

pg.run()



