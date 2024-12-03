# Loan Eligibility Prediction App

This **Loan Eligibility Prediction App** is a machine learning-based web application that predicts whether a person is eligible for a loan based on their provided details. The app uses a **Random Forest model** to make predictions, and it's built with **Streamlit** for an interactive user interface.

## Features
- **Loan Eligibility Prediction**: Predict if a person is eligible for a loan based on their inputs.
- **Probability Display**: Shows the probability of loan eligibility.
- **Custom Design**: Visually appealing with custom background and interactive UI elements.
  
## Technologies Used
- **Python**: Programming language for backend logic and model implementation.
- **Streamlit**: Framework used to build the web app.
- **Scikit-learn**: Library for building and training the machine learning model.
- **Pandas**: Data manipulation and preprocessing.
- **Pickle**: For saving and loading the trained model.
- **CSS**: For styling the app and making it visually attractive.



## Usage

- **Input Fields**: Adjust the sliders and dropdowns in the sidebar to simulate various scenarios.
- **Predictions**: Once you input the data, the model predicts whether you are eligible for a loan and shows the prediction probability.

## Model Explanation

The model used in this application is a **Random Forest Classifier** that was trained on a dataset containing various features such as:
- **Age**
- **Income**
- **Home Ownership**
- **Employment Length**
- **Loan Intent**
- **Loan Grade**
- **Loan Amount**
- **Interest Rate**
- **Credit History**

The model outputs a prediction of either "Eligible" or "Not Eligible" based on the input features, along with the prediction probability.

## Files in the Repository
- `app.py`: The main Streamlit application file.
- `random_forest_loan_model.pkl`: The trained machine learning model.
- `requirements.txt`: A list of Python dependencies required to run the app.
- `README.md`: This file with setup instructions and project information.

## Customization

You can customize the app by:
- Updating the input fields as per your requirements.
- Changing the machine learning model.
- Modifying the visual design by updating the CSS.

## Contributing

If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.


## Contact

For any questions or feedback, feel free to reach out at:
- Email: prathapy150@gmail.com
- GitHub: https://github.com/prathapprr
