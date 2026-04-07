from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

FEATURES = [
    "age","sex","cp","trestbps","chol","fbs",
    "restecg","thalach","exang","oldpeak",
    "slope","ca","thal"
]

@app.post("/predict")
def predict(data: dict):
    try:
        values = [data[f] for f in FEATURES]
        features = np.array(values).reshape(1, -1)
        prediction = model.predict(features)

        return {"prediction": int(prediction[0])}

    except Exception as e:
        return {"error": str(e)}