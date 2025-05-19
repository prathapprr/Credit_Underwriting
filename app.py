import streamlit as st
import joblib
import numpy as np
import pandas as pd
import altair as alt

# Load the pre-trained model
model = joblib.load('model.pkl')

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
# About Us Page

import streamlit as st
import base64
def load_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def about_us_page():
    st.title("👥 Meet the Team")

    st.markdown("""
        <style>
            .intro {
                text-align: center;
                font-size: 18px;
                color: navy;
                margin-bottom: 30px;
                line-height: 1.6;
            }

            .profile-card {
                background: #f9f9f9;
                border-radius: 20px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                animation: fadeIn 1.2s ease;
            }

            .profile-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            }

            .profile-img {
                width: 100%;
                border-radius: 15px;
                transition: transform 0.3s ease-in-out;
                border: 3px solid #eee;
            }

            .profile-card:hover .profile-img {
                transform: scale(1.05);
                border-color: #00bcd4;
            }

            .profile-name {
                font-size: 22px;
                margin-top: 10px;
                color: #222;
                font-weight: bold;
            }

            .profile-role {
                font-size: 15px;
                color: #555;
                margin-bottom: 10px;
            }

            .profile-links a {
                text-decoration: none;
                color: #0077b6;
                font-weight: bold;
                margin: 0 6px;
            }

            .profile-links a:hover {
                color: #ff4081;
            }

            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="intro">
                    🚀 We are a passionate team of developers from <b>Dayananda Sagar Academy of Technology and Management</b>.<br>
        This project <b>"AI-Powered Loan Prediction System"</b> helps banks & financial institutions make smarter decisions using machine learning.<br>
        We're learning, building, and having fun along the way! ✨

        </div>
    """, unsafe_allow_html=True)

    # Columns
    col1, col2, col3 = st.columns(3)

    # Load base64 images
    prathap_img = load_image_base64("Prathap.png.jpg")
    varun_img = load_image_base64("Varun.png.jpg")
    mahesh_img = load_image_base64("Mahesh.png.jpg")

    with col1:
        st.markdown(f"""
        <div class="profile-card">
            <img class="profile-img" src="data:image/jpeg;base64,{prathap_img}" />
            <div class="profile-name">Prathap</div>
            <div class="profile-role">AI & ML Developer<br>Intern @ Infosys</div>
            <div class="profile-links">
                <a href="mailto:prathapy150@gmail.com">📧 Email</a> |
                <a href="https://www.linkedin.com/in/prathap-r-2192442a3/">🔗 LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="profile-card">
            <img class="profile-img" src="data:image/jpeg;base64,{varun_img}" />
            <div class="profile-name">Varun</div>
            <div class="profile-role">Backend Developer<br>APIs & Databases</div>
            <div class="profile-links">
                <a href="varunc3926@gmail.com">📧 Email</a> |
                <a href="https://www.linkedin.com/in/varun-c-89b4a8333/">🔗 LinkedIn</a>
               
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="profile-card">
            <img class="profile-img" src="data:image/jpeg;base64,{mahesh_img}" />
            <div class="profile-name">Mahesh S</div>
            <div class="profile-role">Frontend Dev<br>UI/UX & Streamlit Magic</div>
            <div class="profile-links">
                <a href="maheshgowdamahi1439@gmail.com">📧 Email</a> |
                <a href="https://www.linkedin.com/in/mahesh-s-655903339/">🔗 LinkedIn</a>
                
        """, unsafe_allow_html=True)


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
