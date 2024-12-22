import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Horizontal Navigation Bar
def navigation_bar():
    st.markdown("""
    <style>
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: #f8f9fa;
        padding: 10px;
        border-bottom: 2px solid #dee2e6;
    }
    .nav-bar a {
        text-decoration: none;
        color: #007bff;
        font-size: 18px;
        font-weight: bold;
    }
    .nav-bar a:hover {
        text-decoration: underline;
        color: #0056b3;
    }
    </style>
    <div class="nav-bar">
        <a href="#home">Home</a>
        <a href="#prediction">Prediction</a>
        <a href="#about-us">About Us</a>
        <a href="#faqs">FAQs</a>
    </div>
    """, unsafe_allow_html=True)

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
    st.success("\U0001F4A1 Tip: Use the navigation bar above to explore!")

# About Us Page
def about_us_page():
    st.title("\U0001F4DA About Us")
    st.markdown("""
    **Our Mission**: Simplify financial decision-making with advanced AI tools.

    **About Me**: I am **Prathap**, an **AI Intern** at **Infosys Springboard**. During my internship, I focused on developing
    this Loan Prediction System, working on data preprocessing, model training, and optimization.
    """)
    st.image("aout_dashboard_image.png", caption="Prathap", use_column_width=True)

    with st.expander("\U0001F3D7 System Architecture"):
        st.markdown("""
        The Loan Prediction System comprises:
        - **Frontend**: User-friendly interface built with Streamlit.
        - **Backend**: Pre-trained machine learning model.
        - **Prediction Engine**: Generates real-time results.
        
        Here's a visual representation:
        """)
        st.image("system_architecture.png", caption="System Architecture Diagram", use_column_width=True)

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

# FAQ Page
def faq_page():
    st.title("\U0001F4AC FAQs")
    with st.expander("What factors affect loan approval?"):
        st.write("Factors like credit history, income, loan amount, and dependents play a major role.")
    with st.expander("How accurate is the prediction?"):
        st.write("The model is trained on historical data and has an accuracy of 85%.")
    with st.expander("Can I improve my chances?"):
        st.write("Yes, by improving your credit score and reducing debt.")

# Main Function
def main():
    navigation_bar()
    page = st.selectbox("Select Page", ["Home", "Prediction", "About Us", "FAQs"], key="page_selector", label_visibility="collapsed")

    if page == "Home":
        home_page()
    elif page == "Prediction":
        prediction_page()
    elif page == "About Us":
        about_us_page()
    elif page == "FAQs":
        faq_page()

main()
