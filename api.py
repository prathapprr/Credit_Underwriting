from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('random_forest_loan_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Function to make predictions
def predict_loan_eligibility(input_data):
    prediction = model.predict(input_data)
    return prediction

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Convert the input data into a pandas DataFrame
        input_data = pd.DataFrame([data])

        # Get the prediction
        prediction = predict_loan_eligibility(input_data)

        # Return the prediction as JSON response
        result = {
            'loan_eligibility': 'Eligible' if prediction[0] == 1 else 'Not Eligible'
        }
        return jsonify(result)

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
