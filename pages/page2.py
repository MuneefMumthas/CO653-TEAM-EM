import streamlit as st
import pandas as pd
import time
import base64
import numpy as np
import joblib
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder


#Loading the saved objects
model = tf.keras.models.load_model("pkl/best_model.h5")
mestimate_encoder_ = joblib.load("pkl/mestimate_encoder.pkl")
minmax_scaler = joblib.load("pkl/minmax_scaler.pkl")
label_encoder = joblib.load("pkl/label_encoder.pkl")

st.title("Neural Network 🧠")

st.markdown("---")


def main():
    st.title("Loan Approval Prediction")

    with st.form(key="loan_form"):
        st.subheader("Enter Applicant Details")

        gender = st.selectbox("Gender", ['Select One', 'Male', 'Female'])
        married = st.selectbox("Married", ['Select One', 'Yes', 'No'])
        dependents = st.selectbox("Dependents", ['Select One', '1', '2', '3+'])
        education = st.selectbox("Education", ['Select One', 'Graduate', 'Not Graduate'])
        self_employed = st.selectbox("Self Employed", ['Select One', 'Yes', 'No'])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.number_input("Loan Amount Term (in days)", min_value=0)
        credit_history = st.selectbox("Credit History", ['Select One', 1.0, 0.0])
        property_area = st.selectbox("Property Area", ['Select One', 'Urban', 'Semiurban', 'Rural'])

        submit_btn = st.form_submit_button(label="Test")


if __name__ == "__main__":
    main()

