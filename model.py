import numpy as np
from sklearn.linear_model import LogisticRegression

# Mock training data
# [temperature, humidity, wind_speed, vegetation]
X = np.array([
    [45, 10, 25, 0.9],
    [30, 50, 10, 0.3],
    [40, 20, 20, 0.8],
    [25, 70, 5, 0.2],
    [42, 15, 30, 0.95]
])

y = np.array([1, 0, 1, 0, 1])  # 1 = fire risk, 0 = safe

model = LogisticRegression()
model.fit(X, y)

def predict_fire_risk(data):
    data = np.array(data).reshape(1, -1)  # Ensure the input is a 2D NumPy array
    probability = model.predict_proba(data)[0][1]
    return round(probability * 100, 2)
