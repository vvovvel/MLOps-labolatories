import joblib

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(model_path):
    return joblib.load(model_path)


def predict(model, features):
    prediction = model.predict([features])[0]
    return CLASS_NAMES[prediction]
