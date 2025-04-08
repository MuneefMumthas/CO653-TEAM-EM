import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# === Load Trained Models and Encoders ===
model = tf.keras.models.load_model("pages/pkl/best_model.h5")
mestimate_encoder = joblib.load("pages/pkl/mestimate_encoder.pkl")
minmax_scaler = joblib.load("pages/pkl/minmax_scaler.pkl")
label_encoder = joblib.load("pages/pkl/label_encoder.pkl")
encoder_onehot = joblib.load("pages/pkl/onehot_encoder.pkl")

# === Title ===
st.title("Neural Network 🧠")
st.markdown("---")
st.title("Loan Approval Prediction")

# === Session States ===
if "test_submitted" not in st.session_state:
    st.session_state.test_submitted = False
if "encoded_data" not in st.session_state:
    st.session_state.encoded_data = None

# === Input Form ===
with st.form(key="loan_form"):
    st.subheader("Enter Applicant Details")

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

# === Input Validation ===
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
    if applicant_income == 0 or coapplicant_income == 0:
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

# === Encoding and Scaling ===
if st.session_state.test_submitted:
    st.subheader("📋 Test Input Row")
    st.dataframe(st.session_state.test_input)

    if st.button("Encode & Scale"):
        try:
            df = st.session_state.test_input.copy()

            # Step 1: MEstimate Encoding
            mestimate_cols = ['Gender', 'Married', 'Property_Area', 'Education', 'Self_Employed']
            encoded_mest = mestimate_encoder.transform(df[mestimate_cols])
            encoded_mest = pd.DataFrame(encoded_mest, columns=mestimate_cols)

            # Step 2: OneHot Encoding for Dependents
            dependents_encoded = encoder_onehot.transform(df[['Dependents']])
            dependents_df = pd.DataFrame(dependents_encoded, columns=encoder_onehot.get_feature_names_out(['Dependents']))

            # Step 3: MinMax Scaling
            scale_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'TotalIncome', 'Loan_Amount_Term']
            scaled_values = minmax_scaler.transform(df[scale_cols])
            scaled_df = pd.DataFrame(scaled_values, columns=scale_cols)

            # Step 4: Credit History (not scaled)
            credit_df = df[['Credit_History']].reset_index(drop=True)

            # Final DataFrame
            final_input = pd.concat([
                encoded_mest.reset_index(drop=True),
                dependents_df.reset_index(drop=True),
                scaled_df.reset_index(drop=True),
                credit_df
            ], axis=1)

            st.session_state.encoded_data = final_input
            st.subheader("✅ Final Encoded + Scaled Input")
            st.dataframe(final_input)

        except Exception as e:
            st.error(f"❌ Error during encoding/scaling: {e}")

# === Predict ===
if st.session_state.encoded_data is not None and st.button("Predict Loan Approval"):
    try:
        prediction = model.predict(st.session_state.encoded_data)
        result = (prediction > 0.5).astype(int)
        decoded = label_encoder.inverse_transform(result.ravel())

        st.success(f"🔮 Prediction: {decoded[0]} (Confidence: {prediction[0][0]:.2f})")

    except Exception as e:
        st.error(f"❌ Prediction error: {e}")