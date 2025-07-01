import pandas as pd
import matplotlib.pyplot as plt

# Load stock data
df = pd.read_csv("sample_stock_prices.csv")  # Column is 'ClosingPrice'

# Calculate mean and standard deviation
mean_price = df['ClosingPrice'].mean()
std_dev = df['ClosingPrice'].std()

print("Mean Price:", mean_price)
print("Standard Deviation:", std_dev)

# Plot the stock prices
df['ClosingPrice'].plot(title='Stock Price Over Time')
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()
