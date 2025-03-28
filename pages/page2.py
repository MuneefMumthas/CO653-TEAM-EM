import streamlit as st
import pandas as pd
import time
import base64
import numpy as np
import joblib
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

st.title("Neural Network 🧠")

st.markdown("---")


def main():
    st.title("Loan Approval Prediction")

    # Create a dropdown for users to input new data
    gender = st.selectbox("Gender", ['Male', 'Female'])
    married = st.selectbox("Married", ['Yes', 'No'])
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
    property_area = st.selectbox("Property Area", ['Urban', 'Rural', 'Semiurban'])
    credit_history = st.selectbox("Credit History", ['0', '1'])  # Assume '0' means no and '1' means yes
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_amount_term = st.number_input("Loan Amount Term", min_value=0)
    
    # Prepare the input data as a dictionary
    input_data = {
        'Gender': gender,
        'Married': married,
        'Education': education,
        'Self_Employed': self_employed,
        'Property_Area': property_area,
        'Credit_History': credit_history,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term
    }


if __name__ == "__main__":
    main()

