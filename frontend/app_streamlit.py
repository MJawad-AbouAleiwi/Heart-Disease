import streamlit as st
import requests

st.title("Heart Disease Predictor")

age = st.number_input("Age", 0, 100)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Oldpeak")
slope = st.selectbox("Slope", [0,1,2])
ca = st.number_input("Number of vessels", 0, 4)
thal = st.selectbox("Thal", [0,1,2,3])

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }
    )

    try:
        result = response.json()
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Prediction: {result['prediction']}")
    except:
        st.error("API not responding properly")