import streamlit as st
import pandas as pd
import time
import base64
import numpy as np
import joblib
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder


#Loading the saved objects
model = tf.keras.models.load_model("pages/pkl/best_model.h5")
mestimate_encoder = joblib.load("pages/pkl/mestimate_encoder.pkl")
minmax_scaler = joblib.load("pages/pkl/minmax_scaler.pkl")
label_encoder = joblib.load("pages/pkl/label_encoder.pkl")

st.title("Neural Network 🧠")

st.markdown("---")

st.title("Loan Approval Prediction")

#session state to trac state of buttons
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False

if "prediction_ready" not in st.session_state:
    st.session_state.prediction_ready = False



with st.form(key="loan_form"):
    st.subheader("Enter Applicant Details")

    gender = st.selectbox("What is your Gender", ['Select', 'Male', 'Female'])
    married = st.selectbox("Are you Married", ['Select', 'Yes', 'No'])
    dependents = st.selectbox("Do you have any Dependents", ['Select', '0', '1', '2', '3+'])
    education = st.selectbox("Education", ['Select', 'Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Are you Self Employed", ['Select', 'Yes', 'No'])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
    loan_term = st.selectbox("Loan Amount Term (in months)", ['Select', 12.0, 36.0,60.0,84.0,120.0,180.0,240.0,360.0,480.0])
    credit_history = st.selectbox("Credit History", ['Select', "Good", "Poor"])
    property_area = st.selectbox("Property Area", ['Select', 'Urban', 'Semiurban', 'Rural'])

    submit_btn = st.form_submit_button(label="Submit")


if credit_history == "Good":
    credit_history = 1.0
elif credit_history == "Poor":
    credit_history = 0.0


if submit_btn:
    missing_fields = []
    zero_numbers = []

    if gender == "Select":
        missing_fields.append("Gender")
    if married == "Select":
        missing_fields.append("Married")
    if dependents == "Select":
        missing_fields.append("Dependents")
    if education == "Select":
        missing_fields.append("Education")
    if self_employed == "Select":
        missing_fields.append("Self Employed")
    if credit_history == "Select":
        missing_fields.append("Credit History")
    if property_area == "Select":
        missing_fields.append("Property Area")
    if loan_term == "Select":
        missing_fields.append("Loan Term")

    if applicant_income == 0:
        zero_numbers.append("Applicant Income")
    
    if coapplicant_income == 0:
        zero_numbers.append("Co-Applicant Income")
    

    if missing_fields:
        st.error(f"Please select the required field(s): {', '.join(missing_fields)}", icon="🚨")
        st.toast("💔")
    if zero_numbers:
        st.error(f"Income value needs to be greater than zero: {', '.join(zero_numbers)}", icon="🚨")
        st.toast("💔")
    else:
        total_income = applicant_income + coapplicant_income
        loan_income_ratio = loan_amount/total_income

        user_input = {
            "Gender": gender,
            "Married": married,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,
            "Property_Area": property_area,
            "TotalIncome": total_income,
            "Loan_Income_Ratio": loan_income_ratio,
        }

        st.session_state.test_input = pd.DataFrame([user_input])
        st.session_state.test_submitted = True

    if st.session_state.test_submitted:
        st.subheader("Test Input Row:")
        st.dataframe(st.session_state.test_input)

        if st.button("Encode:"):
            # Apply encoder
            encoded_df = mestimate_encoder.transform(st.session_state.test_input)

            # Combine with numeric fields
            numeric_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Dependents', 'TotalIncome', 'Loan_Income_Ratio']
            encoded_df[numeric_cols] = st.session_state.test_input[numeric_cols]

            # Make sure all columns are in right order
            encoded_scaled = minmax_scaler.transform(encoded_df)

            st.dataframe(encoded_scaled)
            

            