from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Dataset: [symptom1, symptom2], label (0: No condition, 1: Condition)
X = np.array([
    [1, 2], [2, 3], [3, 1],
    [6, 7], [7, 8], [8, 6]
])
y = [0, 0, 0, 1, 1, 1]

# Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Optional hardcoded input (replace with input() for manual entry)
new_patient = np.array([[4.5, 5.0]])
# new_patient = [[float(input("Symptom 1: ")), float(input("Symptom 2: "))]]

# Make prediction
pred = model.predict(new_patient)
proba = model.predict_proba(new_patient)

# Accuracy (evaluated on training data here)
train_pred = model.predict(X)
acc = accuracy_score(y, train_pred)

# Output
print("Prediction (0: No condition, 1: Condition):", pred[0])
print("Prediction probabilities [No, Yes]:", proba[0])
print("Training Accuracy:", round(acc, 2))
