# AI Predictive Models for Credit Underwriting

**Enhance credit underwriting decision-making with AI-driven predictive models.**

---

## Overview

This project utilizes artificial intelligence to improve credit underwriting by predicting the probability of loan defaults based on historical financial data. It offers machine learning models to assist financial institutions in making data-driven decisions with greater accuracy and efficiency.

---

## About

This project aims to leverage machine learning for predictive modeling in credit underwriting. The system predicts the likelihood of a customer defaulting on a loan based on various features, improving decision-making for lenders.

**Key Features:**
- **Predictive Modeling:** Utilizes machine learning algorithms to assess credit risk.
- **Data Preprocessing:** Handles missing values, outlier detection, and categorical encoding.
- **Model Evaluation:** Evaluates models using performance metrics like accuracy, precision, recall, and ROC-AUC.
- **Visual Insights:** Provides visual feedback to help interpret model performance and decision boundaries.

---

## Features

- **Two Web Applications:**
  - **Flask App:** A conventional web application for serving predictions.
  - **Streamlit App:** An interactive dashboard offering easy access to predictions and visualizations.

- **Data Preprocessing:** Includes preprocessing techniques like log transformations and one-hot encoding to clean and prepare data.
- **Pre-trained Model:** A machine learning model (`model.pkl`) that can immediately predict credit risk.

---

## Requirements

To get started, you’ll need Python 3.x and the following libraries:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `streamlit`
- `flask`

---

## Setup

1. **Clone the repository:**

    ```bash
   [ git clone https://github.com/prathapprr/Credit_Underwriting
    cd Credit_Underwriting
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## How It Works

1. **Data Preprocessing:**
   - Clean the dataset by handling missing values and outliers.
   - Encode categorical variables using techniques like one-hot encoding.
   - Split the data into training and testing datasets.

2. **Model Training:**
   - Train models like Logistic Regression, Decision Trees, Random Forests, and Neural Networks.
  
3. **Model Evaluation:**
   - Evaluate model performance using metrics such as:
     - Accuracy
     - Precision
     - Recall
     - F1-score
     - ROC-AUC

4. **Predictions:**
   - Generate predictions for credit risk assessment on new data.

---

## Usage

### 1. **Training and Evaluating Models:**

To train and evaluate the models, simply run:

```bash
python main.py
