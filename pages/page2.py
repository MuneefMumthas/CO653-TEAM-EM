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
    dependants = st.selectbox("Dependants", ['1', '2', '3+'])
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
    

    
    # Prepare the input data as a dictionary
    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependants,
        'Education': education,
        'Self_Employed': self_employed,
    }


if __name__ == "__main__":
    main()

