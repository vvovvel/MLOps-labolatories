import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "model.joblib"


def load_data():
    iris = load_iris()
    return iris.data, iris.target


def train_model(features, labels):
    model = LogisticRegression(max_iter=200)
    model.fit(features, labels)
    return model


def save_model(model, path: str = MODEL_PATH) -> None:
    joblib.dump(model, path)


if __name__ == "__main__":
    features, labels = load_data()
    model = train_model(features, labels)
    save_model(model)
    print(f"Model saved to {MODEL_PATH}")
