from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

# Preprocess input data
def preprocess_data(data):
    gender = data["gender"]
    married = data["married"]
    dependents = data["dependents"]
    education = data["education"]
    employed = data["employed"]
    credit = data["credit"]
    area = data["area"]
    ApplicantIncome = data["ApplicantIncome"]
    CoapplicantIncome = data["CoapplicantIncome"]
    LoanAmount = data["LoanAmount"]
    Loan_Amount_Term = data["Loan_Amount_Term"]

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

# Define routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Loan Prediction API!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        data = request.get_json()

        # Validate input
        required_fields = [
            "gender", "married", "dependents", "education", "employed", 
            "credit", "area", "ApplicantIncome", "CoapplicantIncome", 
            "LoanAmount", "Loan_Amount_Term"
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Preprocess data
        features = preprocess_data(data)

        # Make prediction
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]

        # Prepare response
        result = {
            "prediction": "Approved" if prediction == "Y" else "Rejected",
            "probabilities": {
                "Approved": round(probabilities[1], 2),
                "Rejected": round(probabilities[0], 2)
            }
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/test', methods=['GET'])
def test():
    return "API is working!"


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
