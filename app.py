from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model
from inference import predict as predict_species

MODEL_PATH = "model.joblib"

app = FastAPI()

model = load_model(MODEL_PATH)


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    features = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = predict_species(model, features)
    return PredictResponse(prediction=prediction)
