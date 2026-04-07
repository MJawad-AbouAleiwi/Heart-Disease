# Heart Disease Prediction

## Overview
This project focuses on predicting the presence of heart disease using clinical patient data. The goal is to build and evaluate machine learning models that can accurately classify whether a patient has heart disease, supporting early diagnosis and decision-making.

---

## Dataset

**Source:** UCI Machine Learning Repository – Heart Disease Dataset  

**Description:**  
The dataset contains clinical features describing patient health conditions. It includes 13 attributes such as age, cholesterol level, blood pressure, and heart rate.

- Target variable:
  - 0 → No heart disease  
  - 1 → Presence of heart disease (converted from original multi-class labels)

---

## Project Structure

The notebook follows these main steps:

### 1. Data Loading and Processing
- Load dataset and inspect structure and data types  
- Handle missing values using median and mode imputation  
- Convert target variable into binary classification  

---

### 2. Exploratory Data Analysis
- Analysis of numerical features (age, cholesterol, blood pressure, etc.)  
- Analysis of categorical features (sex, chest pain type, etc.)  
- Target distribution analysis  
- Correlation matrix to identify key predictors  

---

### 3. Modeling and Evaluation

#### Data Preparation
- Train/test split  
- Feature standardization  

#### Models Used
- Logistic Regression  
- Random Forest Classifier 
- Support Vector Classifier
- XGBoost 

#### Hyperparameter Tuning
- GridSearchCV used to optimize model performance  

---

### Model Evaluation

Models are evaluated using:
- Accuracy  
- Precision  
- Recall  
- F1-score  

Performance comparison is conducted to select the best model.

---

### 4. Model Interpretation

- Feature importance analysis using Random Forest  
- Identification of key predictors such as:
  - Chest pain type (cp)  
  - Number of major vessels (ca)  
  - Maximum heart rate (thalach)  
  - ST depression (oldpeak)  

---


## API and Application

To make the model usable in real-world scenarios, it is exposed through a **FastAPI backend** and integrated into an interactive **Streamlit frontend**.

### FastAPI Backend
- Serves the trained model via a REST API  
- Endpoint `/predict` takes patient features as input and returns a prediction  
- Enables model integration into external applications  

### Streamlit Frontend
- Provides a user-friendly interface for entering patient data  
- Sends requests to the API and displays predictions in real time  

---

## Results

- Random Forest achieved the best overall performance  
- The model provides a balanced trade-off between precision and recall  
- Key clinical features were identified as strong indicators of heart disease  

---

## Conclusion

This project demonstrates a complete machine learning pipeline, from data preprocessing and exploration to model training, evaluation, and interpretation. It highlights the importance of combining statistical analysis and machine learning to extract meaningful insights from healthcare data.

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/MJawad-AbouAleiwi/Heart-Disease.git
cd heart-disease
```

### 2. Run the backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### 3. Run the frontend (Streamlit)
```bash
cd frontend
pip install streamlit requests
streamlit run app_streamlit.py
```