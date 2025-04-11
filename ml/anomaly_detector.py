import joblib
import numpy as np

model = joblib.load("ml/model.pkl")

def detect_anomaly(reading):
    X = np.array(reading).reshape(1, -1)
    return model.predict(X)[0] == -1  # -1 = anomaly
