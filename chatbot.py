import streamlit as st
import numpy as np
import google.generativeai as genai
import pandas as pd
import pickle
import joblib
from sklearn.tree import DecisionTreeClassifier

genai.configure(api_key='AIzaSyDTFOeHKJHBwoyXd5sYfFyVwHvFWjuau58')

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.started = False
        st.session_state.current_step = -1
        st.session_state.responses = {}
        st.session_state.show_next_question = True
        
def load_model():
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def preprocess_data(gender, married, dependents, education, employed, credit, area, 
                   ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term):
    try:
        # Existing preprocess_data function remains the same
        male = 1 if gender.lower() == "male" else 0
        married_yes = 1 if married.lower() == "yes" else 0
        if dependents == '1':
            dependents_1, dependents_2, dependents_3 = 1, 0, 0
        elif dependents == '2':
            dependents_1, dependents_2, dependents_3 = 0, 1, 0
        elif dependents == "3+":
            dependents_1, dependents_2, dependents_3 = 0, 0, 1
        else:
            dependents_1, dependents_2, dependents_3 = 0, 0, 0

        not_graduate = 1 if education.lower() == "not graduate" else 0
        employed_yes = 1 if employed.lower() == "yes" else 0
        semiurban = 1 if area.lower() == "semiurban" else 0
        urban = 1 if area.lower() == "urban" else 0

        ApplicantIncomelog = np.log(float(ApplicantIncome))
        totalincomelog = np.log(float(ApplicantIncome) + float(CoapplicantIncome))
        LoanAmountlog = np.log(float(LoanAmount))
        Loan_Amount_Termlog = np.log(float(Loan_Amount_Term))
        if float(credit) <= 1000 and float(credit) >= 800:
            credit = 1
        else:
            credit = 0

        return [
            credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog, totalincomelog,
            male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban
        ]
    except Exception as e:
        st.error(f"Error in preprocessing: {str(e)}")
        return None

def show_chatbot():
    st.title("🤖 Loan Prediction Chatbot")
    st.markdown("""
    Chat with our AI-powered chatbot to get personalized loan predictions.  
    Simply answer the questions, and the chatbot will guide you.
    """)

    # Initialize session state
    initialize_session_state()

    # Define questions
    questions = [
        "What is your gender? (Male/Female)",
        "Are you married? (Yes/No)",
        "How many dependents do you have? (0/1/2/3+)",
        "What is your education level? (Graduate/Not Graduate)",
        "Are you self-employed? (Yes/No)",
        "What is your monthly applicant income?",
        "What is your monthly co-applicant income?",
        "What is the loan amount you are requesting?",
        "What is the loan term in months?",
        "What is your credit history score? (300-850)",
        "What is the area ? (Urban/Semiurban/Rural)"
    ]

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Show initial greeting if not started
    if not st.session_state.started and st.session_state.current_step == -1:
        with st.chat_message("assistant"):
            st.write("Hello! I'm your loan eligibility assistant. Are you ready to begin? (Yes/No)")
    
    # Get user input
    user_input = st.chat_input("Your answer:")

    if user_input:
        # Handle the initial "Are you ready?" response
        if not st.session_state.started:
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            if user_input.lower() == "yes":
                st.session_state.started = True
                st.session_state.current_step = 0
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": '''Great! Let's get started with your loan eligibility assessment:
                                  What is your gender? (Male/Female)  '''
                })
                st.session_state.show_next_question = True
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "No problem! Let me know when you're ready to begin by typing 'Yes'."
                })
            st.rerun()

        # Handle questionnaire responses
        elif st.session_state.current_step < len(questions):
            # Add user response to messages and store it
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.responses[st.session_state.current_step] = user_input

            # Validate input
            valid_input = True
            error_message = ""

            # Input validation based on step
            if st.session_state.current_step in [5, 6, 7, 8]:  # Numeric inputs
                try:
                    float(user_input)
                except ValueError:
                    valid_input = False
                    error_message = "Please enter a valid number."
            elif st.session_state.current_step == 9:  # Credit score
                try:
                    score = float(user_input)
                    if not (0 <= score <= 1000):
                        valid_input = False
                        error_message = "Credit score must be between 0 and 1000."
                except ValueError:
                    valid_input = False
                    error_message = "Please enter a valid credit score."

            if valid_input:
                st.session_state.current_step += 1
                if st.session_state.current_step < len(questions):
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": questions[st.session_state.current_step]
                    })
                st.session_state.show_next_question = True
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })
            st.rerun()

    # Show current question if needed
    # if st.session_state.started and st.session_state.current_step < len(questions) and st.session_state.show_next_question:
    #     with st.chat_message("assistant"):
    #         st.write(questions[st.session_state.current_step])
    #     st.session_state.show_next_question = False

    # Process final results
    if st.session_state.started and st.session_state.current_step == len(questions):
        try:
            # Get all responses
            responses = st.session_state.responses
            
            # Extract all inputs
            gender = responses[0]
            married = responses[1]
            dependents = responses[2]
            education = responses[3]
            self_employed = responses[4]
            applicant_income = responses[5]
            coapplicant_income = responses[6]
            loan_amount = responses[7]
            loan_amount_term = responses[8]
            credit_history = responses[9]
            property_area = responses[10]

            # Process prediction

            st.session_state.messages.append({"role": "assistant", "content": "Here is the information you provided:"})
            captured_info = f"""
            Gender: {gender}
            Marital Status: {married}
            Dependents: {dependents}
            Education: {education}
            Self-Employed: {self_employed}
            Applicant Income: {applicant_income}
            Coapplicant Income: {coapplicant_income}
            Loan Amount: {loan_amount}
            Loan Term: {loan_amount_term}
            Credit History: {credit_history}
            Property Area: {property_area}
            """
            st.session_state.messages.append({"role": "assistant", "content": captured_info})

            with st.chat_message("assistant"):
                st.write("Here is the information you provided:")
                st.write(captured_info)

            # Construct the prompt for prediction (placeholder for future integration)
            st.session_state.messages.append({"role": "assistant", "content": "We will now process your loan eligibility."})
            with st.chat_message("assistant"):
                st.write("We will now process your loan eligibility.")

            # Construct the prompt for Gemini
            prompt = f"""
            I want to check my eligibility for a loan. Here is my information:

Gender: {gender}
Marital Status: {married}
Dependents: {dependents}
Education: {education}
Self-Employed: {self_employed}
Applicant Income: {applicant_income}
Coapplicant Income: {coapplicant_income}
Loan Amount: {loan_amount}
Loan Amount Term: {loan_amount_term}
Credit History: {credit_history}
Property Area: {property_area}
Please evaluate the above details and:

If I am eligible for the loan, provide the next steps to complete the loan process, such as:

Documents I need to prepare.
Steps to finalize the loan application.
Estimated timeline for loan disbursement.
Tips to maintain a good credit score during this process.
If I am not eligible for the loan, kindly suggest actionable steps to improve my eligibility. Specifically:

Areas I should focus on (e.g., increasing income, improving credit history, reducing loan amount).
Recommended credit score improvement strategies.
How to enhance financial stability to meet the loan criteria in the future.
Alternative financing options or smaller loans I might qualify for.
Provide your response in a structured and actionable format to help me take the next steps efficiently.
            """

            if prompt:
                st.session_state.messages.append({"role": "system", "content": prompt})
                # with st.chat_message("system"):
                #     # st.write(prompt)

                # Define Gemini function metadata
                tools = genai.protos.Tool(
                                function_declarations=[
                                    genai.protos.FunctionDeclaration(
                                        name='predict_loan_status',
                                        description="Predicts loan approval status based on user-provided details.",
                                        parameters=genai.protos.Schema(
                                            type=genai.protos.Type.OBJECT,
                                            properties={
                                                "gender": genai.protos.Schema(type=genai.protos.Type.STRING),
                                                "married": genai.protos.Schema(type=genai.protos.Type.STRING),
                                                "dependents": genai.protos.Schema(type=genai.protos.Type.STRING),
                                                "education": genai.protos.Schema(type=genai.protos.Type.STRING),
                                                "self_employed": genai.protos.Schema(type=genai.protos.Type.STRING),
                                                "applicant_income": genai.protos.Schema(type=genai.protos.Type.NUMBER),
                                                "coapplicant_income": genai.protos.Schema(type=genai.protos.Type.NUMBER),
                                                "loan_amount": genai.protos.Schema(type=genai.protos.Type.NUMBER),
                                                "loan_amount_term": genai.protos.Schema(type=genai.protos.Type.NUMBER),
                                                "credit_history": genai.protos.Schema(type=genai.protos.Type.NUMBER),
                                                "property_area": genai.protos.Schema(type=genai.protos.Type.STRING),
                                            },
                                            required=["gender", "married", "education", "applicant_income", "loan_amount", "credit_history", "property_area"]
                                        )
                                    )
                                ]
                            )

            
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        try:
                            # Create the model and start the chat
                            model = genai.GenerativeModel(model_name='gemini-1.5-flash', tools=[tools])
                            chat = model.start_chat(enable_automatic_function_calling=True)
                            response = chat.send_message(prompt)

                            # Log the raw response for debugging purposes (optional)
                            args = ""
                            # st.write(response)
                            for part in response.parts:
                                if fn := part.function_call:
                                    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
                                    print(args)
                                    # st.write(f"{fn.name}({args})")
                            
                            # Initialize the variables
                            loan_amount_term = 0.0
                            coapplicant_income = 0.0
                            applicant_income = 0.0
                            married = ''
                            education = ''
                            property_area = ''
                            self_employed = ''
                            gender = ''
                            loan_amount = 0.0
                            dependents = 0
                            credit_history = 0.0
                            function_name = '' 
                            # Parse the function call arguments and assign them to appropriate variables
                            for part in response.parts:
                                if fn := part.function_call:
                                    function_name = fn.name
                                    for key, val in fn.args.items():
                                        if key == 'loan_amount_term':
                                            loan_amount_term = float(val)  # Expected to be a float
                                        elif key == 'coapplicant_income':
                                            coapplicant_income = float(val)  # Expected to be a float
                                        elif key == 'applicant_income':
                                            applicant_income = float(val)  # Expected to be a float
                                        elif key == 'married':
                                            married = val  # Expected to be a string
                                        elif key == 'education':
                                            education = val  # Expected to be a string
                                        elif key == 'property_area':
                                            property_area = val  # Expected to be a string
                                        elif key == 'self_employed':
                                            self_employed = val  # Expected to be a string
                                        elif key == 'gender':
                                            gender = val  # Expected to be a string
                                        elif key == 'loan_amount':
                                            loan_amount = float(val)  # Expected to be a float
                                        elif key == 'dependents':
                                            dependents = int(val)  # Expected to be an integer
                                        elif key == 'credit_history':
                                            credit_history = float(val)  # Expected to be a float

                            features = preprocess_data(gender, married, dependents, education, self_employed, credit_history, property_area, applicant_income, coapplicant_income, loan_amount, loan_amount_term)
                            model_predicted = load_model()
                            prediction = model_predicted.predict([features])
                            
                            if prediction == 'Y':
                                prediction = 'Eligible for loan'
                                st.balloons()
                                st.markdown("### 🎉 Congratulations! Your loan application is likely approved!")
                            else:
                                prediction = 'Not eligible for loan'
                                st.markdown("### ☠️ Danger! Your loan application has been **rejected**.")
                            
                            response_parts = [
                                    genai.protos.Part(function_response=genai.protos.FunctionResponse(name=function_name, response={"result": prediction}))
                                ]
                            
                            response = chat.send_message(response_parts)
                            st.write(response.text)
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                            st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"})
                            st.stop()

        except Exception as e:
            st.error(f"Error processing results: {str(e)}")

if __name__ == "__main__":
    show_chatbot()