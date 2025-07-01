import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [22, 25, 30, 33, 35, 37]
rainfall = [80, 60, 40, 20, 10, 5]

# Line plot for temperature
plt.plot(months, temperature, marker='o', color='orange')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter plot for rainfall
plt.scatter(months, rainfall, color='blue')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()