import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# Load Trained Models and Encoders
model = tf.keras.models.load_model("pages/pkl/best_model.h5")
mestimate_encoder = joblib.load("pages/pkl/mestimate_encoder.pkl")
minmax_scaler = joblib.load("pages/pkl/minmax_scaler.pkl")
label_encoder = joblib.load("pages/pkl/label_encoder.pkl")
encoder_onehot = joblib.load("pages/pkl/onehot_encoder.pkl")

# Session States
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False
    st.session_state.test_encoded = False
if "encoded_data" not in st.session_state:
    st.session_state.encoded_data = None

from rules import rules

st.title("Fuzzy Logic 📝")

st.markdown("---")

# Input Form
with st.form(key="loan_form"):
    st.subheader("Enter Applicant Details", anchor=False)

    gender = st.selectbox("Gender", ['Select', 'Male', 'Female'])
    married = st.selectbox("Married", ['Select', 'Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Select', '0', '1', '2', '3+'])
    education = st.selectbox("Education", ['Select', 'Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Select', 'Yes', 'No'])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
    loan_term = st.selectbox("Loan Amount Term (months)", ['Select', 12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 360.0, 480.0])
    credit_history = st.selectbox("Credit History", ['Select', "Good", "Poor"])
    property_area = st.selectbox("Property Area", ['Select', 'Urban', 'Semiurban', 'Rural'])

    submit_btn = st.form_submit_button("Submit")

# Input Validation
if credit_history == "Good":
    credit_history = 1.0
elif credit_history == "Poor":
    credit_history = 0.0

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

    # Derived fields
    total_income = applicant_income + coapplicant_income
    loan_income_ratio = loan_amount / total_income

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
        "TotalIncome": total_income,
        "Loan_Income_Ratio": loan_income_ratio
    }])

    st.session_state.test_input = user_input
    st.session_state.test_submitted = True


# Encoding and Scaling
if st.session_state.test_submitted:
    st.dataframe(st.session_state.test_input)
    st.subheader("📋 Preprocess the input data", anchor=False)

    if st.button("Encode & Scale"):
        encoded_df = mestimate_encoder.transform(st.session_state.test_input)

        # Define columns to scale
        columns_for_scaling = [
            'ApplicantIncome',
            'CoapplicantIncome',
            'LoanAmount',
            'TotalIncome',
            'Loan_Amount_Term'
        ]

        # Scale only selected columns
        scaled_values = minmax_scaler.transform(encoded_df[columns_for_scaling])

        # Replace original columns with scaled values
        encoded_df_scaled = encoded_df.copy()
        encoded_df_scaled[columns_for_scaling] = scaled_values

        # Save to session state or display
        st.session_state.encoded_data = encoded_df_scaled

        # One-hot encode Dependents column
        dependents_array = encoder_onehot.transform(encoded_df_scaled[["Dependents"]])

        # Convert to DataFrame with column names like 'Dependents_0', 'Dependents_1', etc.
        dependents_encoded_df = pd.DataFrame(
            dependents_array,
            columns=encoder_onehot.get_feature_names_out(["Dependents"]),
            index=encoded_df_scaled.index  # To preserve row alignment
        )

        # Drop the original "Dependents" column and concatenate one-hot version
        final_df = encoded_df_scaled.drop(columns=["Dependents"])
        final_df = pd.concat([final_df, dependents_encoded_df], axis=1)

        # Save to session and display
        st.session_state.encoded_data = final_df
        
        st.session_state.test_encoded = True

        st.dataframe(st.session_state.encoded_data)


        