import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    'size': [1000, 1500, 2000, 1200],
    'price': [200000, 300000, 400000, 220000]
})

X = df[['size']]
y = df['price']

model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)

# Evaluation
print("Model Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot
plt.scatter(df['size'], df['price'], color='blue')
plt.plot(df['size'], pred, color='red')
plt.title("Size vs Price")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price")
plt.show()