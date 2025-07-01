from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1000, 2], [1500, 3], [2000, 4], [1200, 2]])
y = np.array([200000, 300000, 400000, 220000])

model = LinearRegression()
model.fit(X, y)

# Hardcoded test input (replace with input if needed)
area = 1400
bedrooms = 3
# area = float(input("Area (sqft): "))
# bedrooms = int(input("Number of bedrooms: "))

predicted_price = model.predict([[area, bedrooms]])
print("Predicted price:", predicted_price[0])
