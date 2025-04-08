import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# --- Load trained models and transformers ---
model = tf.keras.models.load_model("pages/pkl/best_model.h5")
mestimate_encoder = joblib.load("pages/pkl/mestimate_encoder.pkl")
minmax_scaler = joblib.load("pages/pkl/minmax_scaler.pkl")
label_encoder = joblib.load("pages/pkl/label_encoder.pkl")

# --- App Title ---
st.title("Neural Network 🧠")
st.markdown("---")
st.title("Loan Approval Prediction")

# --- Session State Initialisation ---
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False
if "encoded_data" not in st.session_state:
    st.session_state.encoded_data = None

# --- Input Form ---
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
    loan_term = st.selectbox("Loan Amount Term (in months)", ['Select', 12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 360.0, 480.0])
    credit_history = st.selectbox("Credit History", ['Select', "Good", "Poor"])
    property_area = st.selectbox("Property Area", ['Select', 'Urban', 'Semiurban', 'Rural'])

    submit_btn = st.form_submit_button(label="Submit")

# --- Data Cleaning and Preparation ---
if credit_history == "Good":
    credit_history = 1.0
elif credit_history == "Poor":
    credit_history = 0.0

if submit_btn:
    # --- Validate inputs ---
    fields = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    missing_fields = [key for key, value in fields.items() if value == "Select"]
    zero_numbers = []
    if applicant_income == 0:
        zero_numbers.append("Applicant Income")
    if coapplicant_income == 0:
        zero_numbers.append("Co-Applicant Income")

    if missing_fields:
        st.error(f"Please select the required field(s): {', '.join(missing_fields)}", icon="🚨")
        st.stop()
    if zero_numbers:
        st.error(f"Income value needs to be greater than zero: {', '.join(zero_numbers)}", icon="🚨")
        st.stop()

    # --- Valid input: prepare input row ---
    total_income = applicant_income + coapplicant_income
    loan_income_ratio = loan_amount / total_income

    user_input = {
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
    }

    input_df = pd.DataFrame([user_input])
    st.session_state.test_input = input_df
    st.session_state.test_submitted = True

# --- Show Test Input ---
if st.session_state.test_submitted:
    st.subheader("🧾 Test Input Row:")
    st.dataframe(st.session_state.test_input)

# --- Encode + Scale on Button Click ---
if st.session_state.test_submitted and st.button("Encode & Scale"):
    try:
        input_df = st.session_state.test_input.copy()

        # 1. Columns
        categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
        numeric_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                        'Loan_Amount_Term', 'Credit_History', 'TotalIncome', 'Loan_Income_Ratio']

        # 2. Encode categorical columns
        encoded_cats = mestimate_encoder.transform(input_df[categorical_cols])
        st.write("✅ Encoded categorical shape:", encoded_cats.shape)

        # 3. Convert to DataFrame with correct column names if possible
        if hasattr(mestimate_encoder, 'get_feature_names_out'):
            encoded_cat_cols = mestimate_encoder.get_feature_names_out(categorical_cols)
        else:
            encoded_cat_cols = categorical_cols  # fallback (generic column names)

        encoded_cat_df = pd.DataFrame(encoded_cats, columns=encoded_cat_cols)

        # 4. Combine with numeric
        numeric_df = input_df[numeric_cols].reset_index(drop=True)
        combined_df = pd.concat([encoded_cat_df.reset_index(drop=True), numeric_df], axis=1)

        st.write("✅ Combined DataFrame shape (before scaling):", combined_df.shape)
        st.dataframe(combined_df)

        # 5. Reorder if scaler remembers training order
        if hasattr(minmax_scaler, 'feature_names_in_'):
            expected_order = list(minmax_scaler.feature_names_in_)
            combined_df = combined_df[expected_order]

        # 6. Scale
        encoded_scaled = minmax_scaler.transform(combined_df)
        scaled_df = pd.DataFrame(encoded_scaled, columns=combined_df.columns)

        st.session_state.encoded_data = encoded_scaled
        st.subheader("🎯 Encoded and Scaled Final Input")
        st.dataframe(scaled_df)

    except Exception as e:
        st.error(f"❌ Error during encoding or scaling: {e}")
            