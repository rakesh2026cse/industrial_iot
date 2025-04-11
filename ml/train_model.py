import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_model():
    df = pd.read_csv("training_data.csv")  # contains historical normal readings
    X = df[['temperature', 'vibration', 'pressure']]
    model = IsolationForest(contamination=0.05)
    model.fit(X)
    joblib.dump(model, "ml/model.pkl")
    print("✅ Model trained and saved.")

if __name__ == "__main__":
    train_model()
