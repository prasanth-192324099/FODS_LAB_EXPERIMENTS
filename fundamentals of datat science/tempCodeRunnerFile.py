import pandas as pd

df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'B'],
    'quantity': [1, 2, 3, 1, 2, 3, 1, 2, 1]
})

top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)
print("Top 5 products:")
print(top_products)
