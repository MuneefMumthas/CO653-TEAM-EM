import streamlit as st
import pandas as pd
import time
import base64


st.set_page_config(
    page_title="LoanEM", 
    page_icon="🏦",
    layout="wide" 
)


# Page Configuration

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

author_details = st.Page(
    page = "pages/page4.py",
    title= "Authors",
    icon = "🫂"
)


# Sidebar Navigation
pg = st.navigation(
    {
        "Info": [home_page],
        "Models":[nn,fuzzy],
        "Comparison": [author_details]
    }
)

st.sidebar.header("Team Members")
st.sidebar.write("- **Enkh-Amgalan Enkhbayar (22135347)**")
st.sidebar.write("- **Muneef Ahamed Mohamed Mumthas (22206529)**")


pg.run()



