import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [2500, 2700, 3000, 3200]

# Line plot
plt.plot(months, sales, marker='o', label='Sales')
plt.title("Monthly Sales (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()

# Bar plot
plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
