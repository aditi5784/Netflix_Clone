Diabetes Risk Prediction System

A Machine Learning–Enabled Clinical Decision Support Web Application

## 1. Introduction

The Diabetes Risk Prediction System is a production-ready Flask web application designed to support preliminary diabetes risk assessment. Using a trained Logistic Regression model, the system evaluates key biometric indicators to determine the user’s diabetes risk category (High / Low) and generates personalized, context-aware health recommendations.

This project is suitable for:

Preventive healthcare systems

Clinical pre-screening workflows

Academic research & demonstrations

Digital health education platforms

## 2. Key Features
# 2.1 Predictive Machine Learning

Logistic Regression classifier trained on the Pima Indians Diabetes Dataset

Fast prediction via serialized model loading (joblib)

Accurate binary classification (High / Low risk)

# 2.2 Personalized Health Advisory Engine

Automatically generates tailored feedback based on:

Glucose levels

BMI & obesity risk

Blood pressure

Insulin resistance patterns

# 2.3 Automated Prediction Logging

Each prediction is recorded in:

data/predictions.csv


This enables traceability, auditability, and long-term data analysis.

# 2.4 Modern, Responsive Web Interface

UI built using HTML, CSS

Secure HTTP POST form handling

Real-time display of risk level & generated advice

## 3. Directory Structure
.
│── app.py                          # Main Flask application

│── train_model.py                  # Model training script


├── model/
 diabetes_model.pkl        # Trained ML model


├── data/
 diabetes.csv ,             # Training dataset
 predictions.csv           # Prediction logs


├── templates/
index.html                # Frontend UI


├── static/style.css                 # Stylesheet

└── README.md                       # Documentation

## 4. Installation & Setup
Step 1: Clone the Repository
git clone <>
cd <project-folder>

Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

Step 3: Install Required Libraries
pip install -r requirements.txt

Step 4: Train the Machine Learning Model (If Needed)
python train_model.py

Step 5: Launch the Application
python app.py

Step 6: Access the Web App

Open your browser and visit:

http://127.0.0.1:5000/

## 5. Requirements / Libraries
requirements.txt
Flask==3.0.0
numpy==1.26.0
pandas==2.1.1
scikit-learn==1.3.1
joblib==1.3.2

## 6. Machine Learning Model Details
Algorithm

Logistic Regression

max_iter = 1000

Training Data

Pima Indians Diabetes Dataset

Target variable: Outcome

Input Features
Feature	Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
BloodPressure	Diastolic blood pressure
SkinThickness	Triceps skinfold thickness
Insulin	Serum insulin
BMI	Body Mass Index
DiabetesPedigreeFunction	Genetic diabetes likelihood
Age	Age in years
## 7. Prediction Logging Specification

Predictions are stored in:

data/predictions.csv


This file contains:

Input values

Calculated risk (High/Low)

Automatically generated advice
