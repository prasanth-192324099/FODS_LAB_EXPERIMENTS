import pandas as pd
from collections import Counter

data = {'age': [25, 30, 22, 30, 28, 25, 35, 30, 22, 25]}
df = pd.DataFrame(data)

freq_dist = df['age'].value_counts().sort_index()
print("Frequency distribution of ages:")
print(freq_dist)
