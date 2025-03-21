import streamlit as st
import pandas as pd
import numpy as np
import time
import base64


st.title("Welcome to Loan-EM", anchor=False)

st.markdown("---")
st.header("Introduction", anchor=False)
st.write(
    "We are developing this system as part of our coursework for **CO653**, where we are required to build a system using either a neural network or fuzzy logic. "
    "However, instead of using these approaches separately, we decided to combine them to leverage their respective strengths."
)

st.markdown("---")
st.header("Methodology", anchor=False)
st.write(
    "Our methodology involves first training the neural network to its optimal performance."
    "Once the neural network has been trained, we will review the importance scores assigned to the various inputs during the training process." 
    "These importance scores help us identify which features have the most influence on the model's predictions."

"Using the information from the importance scores, we will then create rules for the fuzzy logic system. These rules will be designed to align with the decision-making process of the neural network, "
"enabling the fuzzy logic system to approximate the neural network's behaviour. At the same time, the fuzzy logic component will handle uncertainty and imprecision in the input data."

"By combining the neural network and fuzzy logic, we aim to create a robust hybrid model that leverages the learning capabilities of the neural network and the interpretability of fuzzy logic, resulting in a more adaptable and effective solution."

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

train_df = pd.DataFrame(
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
            }, index=pd.Index(range(1, 14))
            )
    
st.dataframe(train_df, height=492)

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
        }, 
        index=pd.Index(range(1, 13))
    )
    
st.dataframe(test_df, height=457)
                     
