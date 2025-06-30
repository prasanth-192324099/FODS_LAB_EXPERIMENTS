import pandas as pd

data = {
    'property_id': [1, 2, 3, 4],
    'location': ['A', 'B', 'A', 'C'],
    'bedrooms': [3, 5, 4, 6],
    'area': [1200, 1500, 1300, 2000],
    'price': [300000, 400000, 350000, 500000]
}

df = pd.DataFrame(data)

print("Average price by location:")
print(df.groupby('location')['price'].mean())

print("\nProperties with >4 bedrooms:", df[df['bedrooms'] > 4].shape[0])

print("\nLargest property:")
print(df.loc[df['area'].idxmax()])
