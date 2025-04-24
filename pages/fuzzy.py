import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
from st_circular_progress import CircularProgress
import time


st.title("new fuzzy", anchor=False)
st.markdown("---")
st.title("Loan Approval Prediction", anchor=False)

# Session States
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False

# Input Form
with st.form(key="loan_form"):
    st.subheader("Enter Applicant Details", anchor=False)

    gender = st.selectbox("Gender", ['Select', 'Male', 'Female'])
    married = st.selectbox("Married", ['Select', 'Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Select', '0', '1', '2', '3+'])
    education = st.selectbox("Education", ['Select', 'Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Select', 'Yes', 'No'])
    applicant_income = st.number_input("Applicant Income (Monthly)", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income (Monthly)", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.selectbox("Loan Amount Term (Months)", ['Select', 'less than 60', 'Between 60 and 120', 'More than 120'])
    credit_history = st.selectbox("Credit History", ['Select', "Good", "Poor"])
    property_area = st.selectbox("Property Area", ['Select', 'Urban', 'Semiurban', 'Rural'])

    submit_btn = st.form_submit_button("Submit")


# Converting applicant income to category
if applicant_income <1500:
    applicant_income = 'Low'

elif applicant_income <= 4000:
    applicant_income = 'Medium'

elif applicant_income > 4000:
    applicant_income = 'High'


# Converting applicant income to category
if coapplicant_income <1500:
    coapplicant_income = 'Low'

elif coapplicant_income <= 4000:
    coapplicant_income = 'Medium'

elif coapplicant_income > 4000:
    coapplicant_income = 'High'

# Converting loan amount to category
if loan_amount < 50000:
    loan_amount = 'Low'

elif loan_amount <= 150000:
    loan_amount = 'Medium'

elif loan_amount > 150000:
    loan_amount = 'High'

# Converting loan term to category
if loan_term == 'less than 60':
    loan_term = 'Short'

elif loan_term == 'Between 60 and 120':
    loan_term = 'Medium'

elif loan_term == 'More than 120':
    loan_term = 'Long'


if submit_btn:
    # Check for missing fields
    fields = {
        "Gender": gender, "Married": married, "Dependents": dependents,
        "Education": education, "Self_Employed": self_employed,
        "Loan_Amount_Term": loan_term, "Credit_History": credit_history,
        "Property_Area": property_area
    }
    missing = [k for k, v in fields.items() if v == "Select"]
    if applicant_income == 0 and coapplicant_income == 0:
        st.error("Applicant/Coapplicant income cannot be zero.", icon="🚨")
        st.stop()
    if missing:
        st.error(f"Missing: {', '.join(missing)}", icon="🚨")
        st.stop()


    # Input as DataFrame
    user_input = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area,
    }])

    st.session_state.test_input = user_input
    st.session_state.test_submitted = True

if st.session_state.test_submitted:
    st.subheader("Your Input",anchor=False)
    st.dataframe(st.session_state.test_input)