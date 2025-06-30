import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample dataset
df = pd.DataFrame({
    'engine_size': [1.2, 1.5, 2.0, 1.8],
    'horsepower': [100, 130, 160, 140],
    'fuel_efficiency': [22, 20, 18, 19],
    'price': [15000, 18000, 25000, 22000]
})

# Features and target
X = df[['engine_size', 'horsepower', 'fuel_efficiency']]
y = df['price']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print model parameters
print("Intercept:", model.intercept_)
print("Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {coef:.2f}")

# Evaluate model performance
y_pred = model.predict(X)
print("R² Score:", r2_score(y, y_pred))

# Predict price for a new car
new_data = pd.DataFrame({
    'engine_size': [1.6],
    'horsepower': [135],
    'fuel_efficiency': [21]
})
predicted_price = model.predict(new_data)
print("Predicted Price for new input:", predicted_price[0])
