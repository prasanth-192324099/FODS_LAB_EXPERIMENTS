import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1500, 1800, 2100, 2500]

# Line Plot
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales (Line)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Scatter Plot
plt.scatter(months, sales, color='red')
plt.title("Monthly Sales (Scatter)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.bar(months, sales, color='green')
plt.title("Monthly Sales (Bar)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
