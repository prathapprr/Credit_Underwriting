
# 🌟 Credit Underwriting using AI 🌟

Welcome to the Credit Underwriting using AI project! This cutting-edge initiative leverages machine learning to empower financial institutions with smarter decision-making in evaluating loan applicants. By predicting the likelihood of loan repayment, it enables more efficient, data-driven credit risk assessments.


## 🚀 Project Overview
This project builds a predictive model using machine learning to estimate the probability of loan default. The aim is to automate and enhance the loan approval process by accurately forecasting whether a borrower will repay the loan.

**Key Features:**
- **AI-driven Credit Risk Prediction**: Utilize historical loan data to predict credit risk.
- **Real-time API Integration**: Expose the model via an API for seamless integration with other applications.
- **Interactive Chatbot**: Allow users to interact with the model and get loan predictions through a conversational interface.

## 🏗 Project Structure
The project is structured as follows to ensure clarity and ease of use:
prathapprr-Credit_Underwriting/
├── README.md                 # Project documentation
├── LICENSE                   # License information
├── Model Building.ipynb      # Notebook for model building and exploration
├── api.py                    # API script for predictions
├── app.py                    # Web application script
├── chatbot.py                # Chatbot interface for querying the model
├── loan-test.csv             # Test dataset for evaluation
├── loan-train.csv            # Training dataset for the model
├── model.pkl                 # Serialized trained model for deployment
├── requirements.txt          # List of dependencies
├── Agile Documentation/      # Agile project management documentation
│   └── PRATHAP_Agile_Documentation.xlsm  # Agile project documentation file
└── .ipynb_checkpoints/       # Jupyter notebook checkpoints
    ├── LICENSE-checkpoint
    └── Model Building-checkpoint.ipynb

## 🌟 Key Features
1. **Machine Learning Model** 🤖  
   - The model is trained using historical loan data to predict the likelihood of loan defaults.  
   - High prediction accuracy achieved using algorithms such as Logistic Regression, Random Forest, and Gradient Boosting.

2. **Real-time API** 🌐  
   - The model is exposed as a RESTful API through `api.py`. This makes it easy to integrate the model into other web services or systems for real-time predictions.

3. **Interactive Chatbot** 💬  
   - The `chatbot.py` file contains a chatbot that allows users to interact with the model by asking questions like:  
     - "Is this person likely to repay the loan?"  
     - "What is the credit risk for this applicant?"

4. **Agile Documentation** 📋  
   - The project follows an Agile methodology for tracking progress and ensuring efficient delivery.  
   - Find the detailed Agile sprint plans and project management documentation in the `Agile Documentation/` folder.


##  🧑‍💻 Installation & Setup



  This repository contains an AI-powered credit underwriting model that can be used to predict creditworthiness based on a given dataset. The project includes a web application to interact with the model and an API for real-time predictions.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation & Setup

Follow the steps below to set up and run the project locally:

### 1. Clone the repository and set up

Clone the repository to your local machine by running:

```bash
git clone https://github.com/prathapprr/Credit_Underwriting.git
cd Credit_Underwriting
```
### 2. Install dependencies

Ensure all required dependencies are installed by running:

```bash
pip install -r requirements.txt
```
### 3. Run the web application

To start the web application locally, run:

```bash
python app.py
```
### 4. Run the API for Predictions

To serve the AI model and make real-time predictions via an API, run:

```bash
python api.py
```
## 🧠 Model Development

The **Model Building.ipynb** notebook contains all necessary steps for developing the credit underwriting model:

1. **Exploratory Data Analysis (EDA)**: 
   - Analyze the dataset to detect patterns and visualize trends.
   
2. **Data Preprocessing**: 
   - Handle missing values, encode categorical variables, and scale numerical data to ensure clean and ready data for training.

3. **Model Training**: 
   - Train various machine learning models, such as Random Forest, Gradient Boosting, etc., to find the best model for credit underwriting prediction.

4. **Model Evaluation**: 
   - Evaluate model performance using metrics such as Accuracy, Precision, Recall, and F1-score to ensure the model's effectiveness.

The trained model is then serialized and stored in `model.pkl` for easy deployment.

## 🤖 Chatbot Integration
### Chatbot Interface

The ``chatbot.py`` file provides a conversational interface that allows users to query the model interactively. Users can ask questions like:

- "What is the likelihood this applicant will repay the loan?"
- "Can you provide a credit score estimate based on this data?"

This chatbot provides an engaging and user-friendly way to interact with the AI model and get real-time predictions based on user input.

## 🧑‍💻 How to Contribute
### Contributing

We welcome contributions from developers and data scientists to improve and expand the project. To contribute:

1. Fork the repository and clone it locally.
2. Create a new branch for your feature or fix.
3. Implement the changes or add new features.
4. Submit a pull request.

Please check the **Issues** section before starting new work to see if the problem has already been reported or addressed.

## 🌱 License
## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as needed. For more information, see the [LICENSE](LICENSE) file.

## 📈 Future Enhancements

### Planned Features:
- **Enhanced Model**: Incorporate advanced algorithms such as XGBoost or Deep Learning for improved prediction accuracy.
- **Data Visualization**: Use tools like Plotly or Matplotlib to visualize insights from the data.
- **Deployment**: Deploy the model and application to platforms such as Heroku or AWS for online accessibility.
- **Mobile App**: Develop a mobile application to interact with the credit underwriting system on the go.

## 💬 Questions or Feedback?
## Contact

Feel free to reach out with any questions or feedback. You can contact me directly at [prathapy150@gmail.com](mailto:prathapy150@gmail.com) or submit an issue via GitHub. Your suggestions are always appreciated!
## 🎯 Project Goals

- **Automate Credit Underwriting**: Revolutionize the credit evaluation process in financial institutions.
- **Promote Financial Inclusion**: Ensure fairer access to credit by minimizing human bias and leveraging data for better decision-making.
- **Scalability & Efficiency**: Build a scalable solution that can process large volumes of loan applications and provide real-time results.

## 🛠 Technologies Used

- **Python**: The backbone of the project for machine learning and backend services.
- **Flask**: Used to build the REST API for model integration.
- **Scikit-learn**: Essential for model training, evaluation, and predictions.
- **Pandas & NumPy**: Used extensively for data manipulation and analysis.
- **Jupyter Notebook**: Ideal for data exploration, model building, and prototyping.

## 🌍 Demo Link


Stay tuned for a live demo link to see the application in action!
