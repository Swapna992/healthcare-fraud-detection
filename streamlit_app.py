
import os
import requests
import streamlit as st
from datetime import datetime, time

st.set_page_config(
    page_title="Healthcare Fraud Detection",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Healthcare Insurance Fraud Detection")
st.write("Enter the details of an insurance claim to estimate its fraud risk.")

# Local API by default; Docker will override this variable.
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

with st.form("claim_form"):
    st.subheader("Claim details")

    claim_id = st.text_input("Claim ID", value="TEST001")
    provider_id = st.text_input("Provider ID", value="PROV001")

    patient_age = st.number_input(
        "Patient age", min_value=0, max_value=120, value=45
    )
    patient_gender = st.selectbox(
        "Patient gender", ["Female", "Male", "Other"]
    )

    diagnosis_code = st.text_input("Diagnosis code", value="DX001")
    procedure_code = st.text_input("Procedure code", value="PR001")

    claim_amount = st.number_input(
        "Claim amount", min_value=0.01, value=10000.0
    )
    approved_amount = st.number_input(
        "Approved amount", min_value=0.0, value=7000.0
    )

    insurance_type = st.text_input("Insurance type", value="Private")
    submission_date = st.date_input(
        "Claim submission date",
        value=datetime(2026, 9, 15).date()
    )

    days_between = st.number_input(
        "Days between service and claim",
        min_value=0, value=5
    )
    provider_claims = st.number_input(
        "Claims per provider per month",
        min_value=0, value=20
    )

    provider_specialty = st.text_input(
        "Provider specialty", value="General Medicine"
    )
    patient_state = st.text_input("Patient state", value="Tamil Nadu")
    claim_status = st.selectbox(
        "Claim status", ["Pending", "Approved", "Rejected"]
    )
    length_of_stay = st.number_input(
        "Length of stay", min_value=0, value=2
    )
    visit_type = st.selectbox(
        "Visit type", ["Inpatient", "Outpatient", "Emergency"]
    )
    chronic_flag = st.selectbox(
        "Chronic condition flag", [0, 1]
    )
    prior_visits = st.number_input(
        "Prior visits in 12 months", min_value=0, value=3
    )

    submitted = st.form_submit_button("Predict fraud risk")

if submitted:
    if approved_amount > claim_amount:
        st.error("Approved amount cannot exceed claim amount.")
    else:
        approval_ratio = approved_amount / claim_amount
        approval_difference = claim_amount - approved_amount

        payload = {
            "Claim_ID": claim_id,
            "Provider_ID": provider_id,
            "Patient_Age": patient_age,
            "Patient_Gender": patient_gender,
            "Diagnosis_Code": diagnosis_code,
            "Procedure_Code": procedure_code,
            "Claim_Amount": claim_amount,
            "Approved_Amount": approved_amount,
            "Insurance_Type": insurance_type,
            "Claim_Submission_Date": (
                f"{submission_date.isoformat()}T10:30:00"
            ),
            "Days_Between_Service_and_Claim": days_between,
            "Number_of_Claims_Per_Provider_Monthly": provider_claims,
            "Provider_Specialty": provider_specialty,
            "Patient_State": patient_state,
            "Claim_Status": claim_status,
            "Length_of_Stay": length_of_stay,
            "Visit_Type": visit_type,
            "Chronic_Condition_Flag": chronic_flag,
            "Prior_Visits_12m": prior_visits,
            "Approval_Ratio": approval_ratio,
            "Claim_Approval_Difference": approval_difference,
            "Claim_Year": submission_date.year,
            "Claim_Month": submission_date.month,
            "Claim_DayOfWeek": submission_date.weekday()
        }

        try:
            with st.spinner("Getting prediction..."):
                response = requests.post(
                    f"{API_URL}/predict",
                    json=payload,
                    timeout=30
                )

            if response.status_code == 200:
                result = response.json()

                probability = float(result["fraud_probability"])
                risk = result["risk_category"]

                st.subheader("Prediction result")
                st.metric(
                    "Estimated fraud probability",
                    f"{probability:.2%}"
                )
                st.write(f"**Risk category:** {risk}")
                st.info(
                    "This is a model-generated risk estimate, "
                    "not proof of fraud. Review the claim before "
                    "making any decision."
                )
            else:
                st.error(
                    f"API returned {response.status_code}: "
                    f"{response.text}"
                )

        except requests.RequestException as error:
            st.error(
                f"Could not connect to the prediction API: {error}"
            )
