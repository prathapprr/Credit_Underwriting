import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
with open('random_forest_loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Apply custom CSS for background and styling
def apply_custom_css():
    st.markdown("""
    <style>
    /* Add background image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1542728928-1413d1894ed4?crop=entropy&cs=tinysrgb&w=1200');
        background-size: cover;
        background-position: center;
        color: white;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: rgba(0, 0, 0, 0.6);
        color: white;
        padding: 10px;
        border-radius: 10px;
    }
    /* Header styling */
    h1, h2, h3 {
        color: #f4f4f4;
        font-family: 'Arial', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    /* Button styling */
    .stButton>button {
        background: #ff7f50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: #ff4500;
    }
    </style>
    """, unsafe_allow_html=True)

# Apply the custom CSS
apply_custom_css()

# Title and description
st.title("🌟 Loan Eligibility Prediction App 🌟")
st.markdown("""
Welcome to the **Loan Eligibility Prediction App**. This visually appealing tool allows you to predict loan eligibility with ease. Adjust the sliders and dropdowns to input details, and let the model do the work!
""")

# Sidebar for inputs
st.sidebar.header("🔧 Input Features")
def user_input():
    person_age = st.sidebar.slider("Age", 18, 100, 30)
    person_income = st.sidebar.number_input("Annual Income ($)", value=50000, step=1000)
    person_home_ownership = st.sidebar.selectbox("Home Ownership", ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
    person_emp_length = st.sidebar.slider("Employment Length (Years)", 0, 50, 5)
    loan_intent = st.sidebar.selectbox("Loan Intent", ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])
    loan_grade = st.sidebar.selectbox("Loan Grade", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    loan_amnt = st.sidebar.number_input("Loan Amount ($)", value=10000, step=500)
    loan_int_rate = st.sidebar.slider("Loan Interest Rate (%)", 5.0, 30.0, 15.0)
    loan_percent_income = st.sidebar.slider("Loan Percent Income", 0.0, 1.0, 0.2)
    cb_person_default_on_file = st.sidebar.selectbox("Default on Credit Before?", ['Y', 'N'])
    cb_person_cred_hist_length = st.sidebar.slider("Credit History Length (Years)", 1, 30, 5)
    
    data = pd.DataFrame({
        'person_age': [person_age],
        'person_income': [person_income],
        'person_home_ownership': [person_home_ownership],
        'person_emp_length': [person_emp_length],
        'loan_intent': [loan_intent],
        'loan_grade': [loan_grade],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_default_on_file': [cb_person_default_on_file],
        'cb_person_cred_hist_length': [cb_person_cred_hist_length]
    })
    return data

input_data = user_input()

# Display user inputs
st.subheader("📋 User Input Parameters")
st.write(input_data)

# Preprocess inputs
def preprocess_input(data):
    label_mappings = {
        'person_home_ownership': {'RENT': 0, 'OWN': 1, 'MORTGAGE': 2, 'OTHER': 3},
        'loan_intent': {'PERSONAL': 0, 'EDUCATION': 1, 'MEDICAL': 2, 'VENTURE': 3, 'HOMEIMPROVEMENT': 4, 'DEBTCONSOLIDATION': 5},
        'loan_grade': {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6},
        'cb_person_default_on_file': {'N': 0, 'Y': 1}
    }
    for col, mapping in label_mappings.items():
        data[col] = data[col].map(mapping)
    return data

processed_data = preprocess_input(input_data)

# Prediction
prediction = model.predict(processed_data)
prediction_proba = model.predict_proba(processed_data)

# Display prediction results
st.subheader("📊 Prediction Result")
loan_status = "✅ Eligible" if prediction[0] == 1 else "❌ Not Eligible"
st.write(f"Loan Status: **{loan_status}**")

st.subheader("📈 Prediction Probability")
st.write(f"Probability of Eligibility: **{prediction_proba[0][1] * 100:.2f}%**")
