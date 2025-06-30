import numpy as np

# Step 1: Manually include the dataset as a NumPy array
# Each row = [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1200, 250000],
    [5, 2400, 500000],
    [4, 1800, 350000],
    [6, 3000, 650000],
    [2, 900, 200000],
    [5, 2600, 520000],
    [4, 2100, 430000],
    [3, 1600, 280000],
    [6, 3100, 670000],
    [2, 800, 180000],
    [5, 2200, 480000],
    [4, 1900, 390000],
    [3, 1500, 260000],
    [6, 3200, 700000],
    [2, 850, 190000],
    [5, 2700, 550000],
    [4, 2000, 410000],
    [3, 1400, 240000],
    [6, 3300, 720000],
    [2, 750, 175000]
])

filtered_houses = house_data[house_data[:, 0] > 4]

sale_prices = filtered_houses[:, 2]

average_price = np.mean(sale_prices)

print("Average sale price of houses with more than 4 bedrooms:", round(average_price, 2))
