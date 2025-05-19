import streamlit as st
import requests

# Google Gemini API Key (Replace with your actual key)
API_KEY = "YOUR_GEMINI_API_KEY"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Streamlit UI
st.title("Google Gemini AI Chatbot 🤖")
st.write("Ask anything, and Gemini AI will respond!")

# User input
user_prompt = st.text_area("Enter your prompt:", "Explain how AI works")

if st.button("Generate Response"):
    if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY":
        st.error("Please replace `YOUR_GEMINI_API_KEY` with a valid API key.")
    elif not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            # Prepare request data
            headers = {"Content-Type": "application/json"}
            data = {"contents": [{"parts": [{"text": user_prompt}]}]}

            # Send API request
            response = requests.post(URL, headers=headers, json=data)

            # Display response
            if response.status_code == 200:
                result = response.json()
                try:
                    text_response = result["candidates"][0]["content"]["parts"][0]["text"]
                    st.success("Response:")
                    st.write(text_response)
                except KeyError:
                    st.error("Unexpected response format. Please check API response.")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
