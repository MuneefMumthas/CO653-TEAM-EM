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

# Load the pre-trained model
model = tf.keras.models.load_model('pkl/best_model.h5')

# Load the encoders
encoder_gender = joblib.load('encoder_gender.pkl')
encoder_married = joblib.load('encoder_married.pkl')
encoder_education = joblib.load('encoder_education.pkl')
encoder_self_employed = joblib.load('encoder_self_employed.pkl')
encoder_property_area = joblib.load('encoder_property_area.pkl')
encoder_credit_history = joblib.load('encoder_credit_history.pkl')

# Define a function to preprocess input data using the encoders
def preprocess_input_data(data):
    # Apply label encoders to categorical features
    data['Gender'] = encoder_gender.transform([data['Gender']])
    data['Married'] = encoder_married.transform([data['Married']])
    data['Education'] = encoder_education.transform([data['Education']])
    data['Self_Employed'] = encoder_self_employed.transform([data['Self_Employed']])
    data['Property_Area'] = encoder_property_area.transform([data['Property_Area']])
    data['Credit_History'] = encoder_credit_history.transform([data['Credit_History']])

    return data


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

    # Create a dataframe from the input data
    input_df = pd.DataFrame([input_data])

    # Preprocess input data
    processed_input = preprocess_input_data(input_df)

    # Make the prediction
    prediction = model.predict(processed_input)

    # Display the result
    if prediction[0] > 0.5:
        st.write("Loan Approved")
    else:
        st.write("Loan Denied")

if __name__ == "__main__":
    main()

