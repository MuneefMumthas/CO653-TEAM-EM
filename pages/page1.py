import streamlit as st
import pandas as pd
import time
import base64

st.title("Welcome to CO653 - Loan Prediction 👋")

st.header("Data Dictionary")

st.subheader("Train file: CSV containing the customers for whom loan eligibility is known as 'Loan_Status'")
st.write(
    pd.DataFrame(
    {
        "Variable": [
            "Loan_ID", "Gender", "Married", "Dependents", "Education", 
            "Self_Employed", "ApplicantIncome", "CoapplicantIncome", 
            "LoanAmount", "Loan_Amount_Term", "Credit_History", 
            "Property_Area", "Loan_Status"
        ],
        "Description": [
            "Unique Loan ID", "Male/ Female", "Applicant married (Y/N)", 
            "Number of dependents", "Applicant Education (Graduate/ Under Graduate)", 
            "Self employed (Y/N)", "Applicant income", "Coapplicant income", 
            "Loan amount in thousands", "Term of loan in months", 
            "Credit history meets guidelines", "Urban/ Semi Urban/ Rural", 
            "(Target) Loan approved (Y/N)"
        ]
    }
    )
    
    )

st.subheader("Test file: CSV containing the customer information for whom loan eligibility is to be predicted")
st.write(
    pd.DataFrame(
    {
        "Variable": [
            "Loan_ID", "Gender", "Married", "Dependents", "Education", 
            "Self_Employed", "ApplicantIncome", "CoapplicantIncome", 
            "LoanAmount", "Loan_Amount_Term", "Credit_History", 
            "Property_Area"
        ],
        "Description": [
            "Unique Loan ID", "Male/ Female", "Applicant married (Y/N)", 
            "Number of dependents", "Applicant Education (Graduate/ Under Graduate)", 
            "Self employed (Y/N)", "Applicant income", "Coapplicant income", 
            "Loan amount in thousands", "Term of loan in months", 
            "Credit history meets guidelines", "Urban/ Semi Urban/ Rural"
        ]
    }
    )
    
    )
                     

st.write("something here...")