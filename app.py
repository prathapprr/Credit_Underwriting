import streamlit as st
import pickle
import numpy as np
import pandas as pd
import altair as alt

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Prediction", "Dashboard", "Calculator", "About Us", "FAQs"])
    return page

# Home Page
def home_page():
    st.title("\U0001F680 Loan Prediction System")
    st.markdown("### \U0001F4DD **Welcome to the Loan Prediction System!**")
    st.image("loan.png", caption="Loan Prediction System", use_column_width=True)

    with st.expander("\U0001F4C8 Project Overview"):
        st.markdown("""
        This project was developed as part of my **AI internship** at **Infosys Springboard**.
        It aims to predict whether a loan application will be approved or rejected using machine learning.
        
        **Key Features:**
        - Easy-to-use interface.
        - Accurate predictions using pre-trained models.
        - Financial insights for better decision-making.
        
        **New Additions:**
        - Enhanced visualization of prediction probabilities.
        - User guidance for improving approval chances.
        - Multiple language support (coming soon).
        """)
    st.success("\U0001F4A1 Tip: Use the sidebar to navigate!")

# Prediction Page
def prediction_page():
    st.title("\U0001F4C8 Loan Prediction System")
    st.markdown("### \U0001F4D8 Enter your details below to predict loan status")

    # User input fields
    gender = st.selectbox("\U0001F464 Gender", ["Male", "Female"], help="Select your gender.")
    married = st.selectbox("\U0001F492 Marital Status", ["Yes", "No"], help="Are you married?")
    dependents = st.selectbox("\U0001F46A Dependents", ["0", "1", "2", "3+"], help="Number of dependents.")
    education = st.selectbox("\U0001F393 Education", ["Graduate", "Not Graduate"], help="Select your education level.")
    employed = st.selectbox("\U0001F4BC Self Employed", ["Yes", "No"], help="Are you self-employed?")
    credit = st.slider("\U0001F4B0 Credit History", 0.0, 1.0, 0.5, step=0.01, help="Enter your credit history score.")
    area = st.selectbox("\U0001F3E1 Property Area", ["Urban", "Semiurban", "Rural"], help="Choose your property area.")
    ApplicantIncome = st.slider("\U0001F4B5 Applicant Income", 1000, 100000, 5000, step=1000, help="Enter your income.")
    CoapplicantIncome = st.slider("\U0001F91D Coapplicant Income", 0, 100000, 0, step=1000, help="Income of co-applicant.")
    LoanAmount = st.slider("\U0001F4B3 Loan Amount", 1, 100000, 100, step=10, help="Requested loan amount.")
    Loan_Amount_Term = st.select_slider("\U0001F4C5 Loan Amount Term (days)", options=[360, 180, 240, 120], value=360, help="Choose loan term.")

    def preprocess_data(*args):
        gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term = args
        male = 1 if gender == "Male" else 0
        married_yes = 1 if married == "Yes" else 0
        dependents_1 = dependents == "1"
        dependents_2 = dependents == "2"
        dependents_3 = dependents == "3+"
        not_graduate = 1 if education == "Not Graduate" else 0
        employed_yes = 1 if employed == "Yes" else 0
        semiurban = 1 if area == "Semiurban" else 0
        urban = 1 if area == "Urban" else 0
        return [
            credit, np.log(ApplicantIncome), np.log(LoanAmount), np.log(Loan_Amount_Term), np.log(ApplicantIncome + CoapplicantIncome),
            male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban
        ]

    if st.button("\U0001F50D Predict Loan Status"):
        features = preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term)
        with st.spinner("Analyzing your data..."):
            prediction = model.predict([features])[0]
            probabilities = model.predict_proba([features])[0]

        st.write("### Prediction Probabilities")
        st.progress(int(probabilities[1] * 100))

        if prediction == "N":
            st.error("\U0001F6AB Loan Status: Rejected")
            st.markdown("- Improve credit history\n- Adjust loan amount or term\n- Review financial details")
            st.image("rejected.png", caption="Loan Rejected", use_column_width=True)
        else:
            st.success("\U00002705 Loan Status: Approved")
            st.image("approved.png", caption="Loan Approved", use_column_width=True)

# Dashboard Page
def dashboard_page():
    st.title("\U0001F4CA Dashboard")
    st.markdown("### Insights and Trends")

    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Approvals": [30, 45, 50, 65, 70],
        "Rejections": [20, 25, 30, 20, 15]
    }
    df = pd.DataFrame(data)

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Month", sort=None),
        y=alt.Y("Approvals", title="Loan Approvals"),
        color=alt.Color("Month", legend=None)
    ).properties(
        title="Monthly Loan Approvals"
    )

    st.altair_chart(chart, use_container_width=True)

# Loan Calculator Page
def calculator_page():
    st.title("\U0001F4B8 Loan EMI Calculator")
    st.markdown("### Calculate your loan repayment schedule")

    principal = st.number_input("Loan Amount", min_value=1000, step=1000, help="Enter the loan amount")
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.1, step=0.1, help="Annual interest rate")
    tenure_years = st.number_input("Loan Tenure (Years)", min_value=1, step=1, help="Duration of the loan in years")

    if st.button("Calculate EMI"):
        r = (interest_rate / 100) / 12
        n = tenure_years * 12
        emi = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        st.success(f"Your monthly EMI is: \u20B9{emi:.2f}")

# About Us Page
def about_us_page():
    st.title("\U0001F465 About Us")
    st.markdown("""
    Welcome to the Loan Prediction System developed during my AI internship at Infosys Springboard.

    **Developer:** Prathap  
    **Contact:** [Email](mailto:prathapy150gmail.com) | [LinkedIn](https://www.linkedin.com/in/prathap-r-2192442a3/)

    This system was built using:
    - Python and Streamlit for the frontend
    - Machine learning model for predictions
    - Visualization tools like Altair and Pandas for data analysis
    """)
    st.image("about_dashboard_image.png", caption="Loan Prediction System", use_column_width=True)

# FAQs Page
def faq_page():
    st.title("\U0001F4AC FAQs")
    st.markdown("""
    **1. How does the system work?**  
    - It uses a pre-trained machine learning model to predict loan approval.

    **2. What data is needed for prediction?**  
    - User details like income, loan amount, credit history, etc.

    **3. How accurate is the prediction?**  
    - The system is trained on real-world data with high accuracy.

    For more queries, contact us via [Email](mailto:prathapy150gmail.com).
    """)

# Main Function
def main():
    page = sidebar_navigation()

    if page == "Home":
        home_page()
    elif page == "Prediction":
        prediction_page()
    elif page == "Dashboard":
        dashboard_page()
    elif page == "Calculator":
        calculator_page()
    elif page == "About Us":
        about_us_page()
    elif page == "FAQs":
        faq_page()

if __name__ == "__main__":
    main()
