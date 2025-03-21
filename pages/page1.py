import streamlit as st
import pandas as pd
import numpy as np
import time
import base64


st.title("Welcome to CO653 - Loan-EM", anchor=False)

st.markdown("---")
st.header("Introduction", anchor=False)
st.write(
    "We are developing this system as part of our coursework for CO653, where we are required to build a system using either a neural network or fuzzy logic. "
    "However, we decided to implement both approaches to compare their performance."
)

st.markdown("---")
st.header("Dataset", anchor=False)
st.write(
    "For our dataset, we found one from a hackathon, which we are utilising to train and evaluate our models. "
    "While our primary goal is to complete the coursework assignment, we are also using the hackathon as an opportunity to review our model's score on the leaderboard,"
    "essentially hitting two birds with one stone."
)

st.markdown("---")
st.header("About the Hackathon", anchor=False)
st.write(
    "[Analytics Vidhya Loan Prediction Challenge.](https://www.analyticsvidhya.com/datahack/contest/practice-problem-loan-prediction-iii/) "
)
st.write(
    "Participants must build a model to predict loan approval based on applicant details. "
    "Evaluation is based on **accuracy**, and top models will be featured on the leaderboard."
)

st.markdown("---")
st.header("Data Dictionary", anchor=False)

st.subheader("Train file: ", anchor=False)
st.write("CSV containing the customers for whom loan eligibility is known as 'Loan_Status'")


#dowload button for train file
@st.cache_data
def get_data():
    return pd.read_csv("data/Loan_train.csv")

#convert DataFrame to CSV for download
@st.cache_data
def convert_for_download(df):
    return df.to_csv(index=False).encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download Train Dataset CSV",
    data=csv,
    file_name="Loan_train.csv",
    mime="text/csv",
    icon=":material/download:",
)

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

st.subheader("Test file:", anchor=False)
st.write("CSV containing the customer information for whom loan eligibility is to be predicted")

#dowload button for test file
@st.cache_data
def get_data():
    return pd.read_csv("data/Loan_test.csv")

#convert DataFrame to CSV for download
@st.cache_data
def convert_for_download(df):
    return df.to_csv(index=False).encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download Test Dataset CSV",
    data=csv,
    file_name="Loan_test.csv",
    mime="text/csv",
    icon=":material/download:",
)

test_df = pd.DataFrame(
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
    
st.dataframe(test_df)
                     
