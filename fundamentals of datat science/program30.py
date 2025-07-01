from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import r2_score
import pandas as pd

# Define dataset
data = pd.DataFrame({
    "mileage": [20000, 50000, 15000, 30000],
    "age": [3, 5, 2, 4],
    "brand": [1, 2, 1, 2],  # 1 = Brand A, 2 = Brand B
    "engine": [1, 2, 2, 1],  # 1 = Petrol, 2 = Diesel
    "price": [15000, 10000, 17000, 12000]
})

# Features and target
X = data[["mileage", "age", "brand", "engine"]]
y = data["price"]

# Model training
model = DecisionTreeRegressor(random_state=0)
model.fit(X, y)

# Evaluate model
y_pred = model.predict(X)
print("R² Score on training data:", r2_score(y, y_pred))

# Predict new input (you can change these values for testing)
new_car = pd.DataFrame([{
    "mileage": 25000,
    "age": 3,
    "brand": 1,
    "engine": 2
}])

prediction = model.predict(new_car)
print("Predicted Price for new car:", prediction[0])

# Show decision tree logic
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n", tree_rules)
