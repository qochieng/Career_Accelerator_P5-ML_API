import pandas as pd 
import pickle,joblib, os
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class SepssisFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

random_forest_pipeline = joblib.load("./models/RandomForest.pkl")
logistic_regression_pipeline = joblib.load("./models/LogisticRegression.pkl")
decision_tree_pipeline = joblib.load("./models/Decision_Tree.pkl")


def encoder():
    encoder = joblib.load("./models/label_encoder.pkl")

    return encoder


@app.get("/")
def homepage():
    return {"message": "Patient Sepssis Predict"}

@app.post("/random_forest_predict")
def random_forest_prediction(data:SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])
    
    prediction = random_forest_pipeline.predict(df)

    prediction = int(prediction[0])
    prediction = encoder().inverse_transform([prediction])[0]
    probability = random_forest_pipeline.predict_proba(df)
    probabilities = probability.tolist()

    return {'Sepssis Predictions': prediction,'Probabilities': probabilities}

@app.post("/logistic_regression_predict")
def logistic_regression_prediction(data:SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])
    
    prediction = logistic_regression_pipeline.predict(df)

    prediction = int(prediction[0])
    prediction = encoder().inverse_transform([prediction])[0]
    probability = logistic_regression_pipeline.predict_proba(df)
    probabilities = probability.tolist()

    return {'Sepssis Predictions': prediction,'Probabilities': probabilities}

@app.post("/decision_tree_predict")
def decision_tree_prediction(data:SepssisFeatures):
    df = pd.DataFrame([data.model_dump()])
    
    prediction = decision_tree_pipeline.predict(df)

    prediction = int(prediction[0])
    prediction = encoder().inverse_transform([prediction])[0]
    probability = decision_tree_pipeline.predict_proba(df)
    probabilities = probability.tolist()

    return {'Sepssis Predictions': prediction,'Probabilities': probabilities}


@app.get('/Documentation')
def documentation():
    return {'Documentation':'all documentation'}
