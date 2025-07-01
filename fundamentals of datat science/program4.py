import numpy as np
import matplotlib.pyplot as plt

sales_data = np.array([150000, 180000, 210000, 250000])
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

total_sales = np.sum(sales_data)

percentage_increase_q1_q4 = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

quarterly_increases = [
    ((sales_data[i+1] - sales_data[i]) / sales_data[i]) * 100
    for i in range(len(sales_data) - 1)
]

plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, sales_data, color='skyblue')
plt.title("Quarterly Sales Analysis", fontsize=16)
plt.xlabel("Quarters")
plt.ylabel("Sales Amount (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5000, f'{int(yval)}', 
             ha='center', va='bottom', fontsize=10)
for i in range(len(quarterly_increases)):
    x_pos = (i + 0.5)
    y_pos = max(sales_data[i], sales_data[i+1]) + 20000
    plt.text(x_pos, y_pos, f"+{round(quarterly_increases[i], 2)}%", 
             ha='center', fontsize=10, color='green')

plt.text(1.5, max(sales_data) + 50000, 
         f"Q1 → Q4 Total Increase: {round(percentage_increase_q1_q4, 2)}%", 
         ha='center', fontsize=12, color='red', weight='bold')

plt.ylim(0, max(sales_data) + 80000)
plt.tight_layout()
plt.show()
