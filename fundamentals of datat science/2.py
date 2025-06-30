import numpy as np

sales_data = np.array([
    [10, 30, 100, 5],  
    [15, 46, 300, 10],  
    [20, 30, 600, 0]    
])

total_quantities = np.sum(sales_data[:, 0])     
total_revenue = np.sum(sales_data[:, 2])         

avg_price = total_revenue / total_quantities

average_discount = np.mean(sales_data[:, 3])    

print("Average price of all products sold:", round(avg_price, 2))
print("Average discount offered:", round(average_discount, 2), "%")
