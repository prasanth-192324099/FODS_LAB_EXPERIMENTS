import pandas as pd

data = {
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': pd.to_datetime(['2024-01-01', '2024-01-03', '2024-01-10', '2024-01-15', '2024-01-20']),
    'product': ['A', 'B', 'A', 'C', 'B'],
    'quantity': [1, 2, 1, 3, 2]
}

df = pd.DataFrame(data)

print("Orders per customer:")
print(df.groupby('customer_id').size())

print("\nAverage quantity per product:")
print(df.groupby('product')['quantity'].mean())

print("\nEarliest and latest order dates:")
print(df['order_date'].min(), "to", df['order_date'].max())
