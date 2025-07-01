from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([
    [300, 12],
    [100, 6],
    [400, 24],
    [150, 3]
])
y = [0, 1, 0, 1]

model = LogisticRegression(random_state=42)
model.fit(X, y)

new_customer = np.array([[250, 6]])
# usage = float(input("Usage minutes: "))
# contract = int(input("Contract duration (months): "))
# new_customer = np.array([[usage, contract]])

pred = model.predict(new_customer)
proba = model.predict_proba(new_customer)

print("Churn Prediction (0: No, 1: Yes):", pred[0])
print("Churn Probability [No, Yes]:", proba[0])
