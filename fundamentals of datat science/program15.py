import pandas as pd

likes_data = {'likes': [5, 10, 5, 20, 10, 10, 5, 15, 20, 5]}
df = pd.DataFrame(likes_data)

frequency = df['likes'].value_counts().sort_index()
print("Frequency of likes:")
print(frequency)
