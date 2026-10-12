HEALTHCARE INSURANCE FRAUD DETECTION:

Project Overview:

This project uses machine learning to predict whether a healthcare insurance claim is potentially fraud.

The objective is to assign a fraud probability to incoming claims and categorize them into Low, Medium and High Risk so that suspicious claims can be prioritized for manual investigation.

Dataset:
The dataset contains 10,000 healthcare insuramce claims and 20 features.

The target variable is:
- Is_Fraud = 0 ---> Genuine claim
- Is_Fraud = 1 ---> Fraudulent claim

The dataset was obtained from Kaggle.

Key Features:
The dataset contains information about:
- Patient demographics
- Diagnosis
- Procedure
- Claim amount
- Approved amount
- Insurance type
- Provider speciality
- Patient state
- Claim status
- Length of stay
- Previous visits
- Provider monthly claim volume

MACHINE LEARNING APPROACH:
- Data loading
- Data understanding
- Exploratory Data Analysis
- Missing and duplicate value analysis
- Feature Engineering
- Train-Test split
- Categorical encoding
- Numerical feature scaling 
- Class-imbalance handling
- Logistic Regression
- Random Forest
- Model Evaluation
- Fraud probability prediction 
- Risk categorization
- Model serialization

FEATURE ENGINEERING:
This project creates additional features:
- Approval Ratio
- Claim Approval Difference
- Claim Year
- Claim Month
- Claim Year

MODEL EVALUATION:
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Accuracy is not used because fradulent claims represent a minority class.

BUSINESS USE CASE:
The final model produces a fraud probability for each claim:
EXAMPLE:
Fraud Probability.       Risk 
0.15                     Low Risk
0.52                     Medium Risk
0.88                     High Risk

High risk claims can be prioritized for manual investigation.

LIBRARIES:
Pandas
Numpy
Scikit-learn
Matplotlib
Seaborn
joblib
jupyter
fastapi
uvicorn[standard]
streamlit
requests
pydantic