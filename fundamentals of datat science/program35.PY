import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample transaction data
df = pd.DataFrame({
    'amount_spent': [100, 200, 300, 400, 250, 600],
    'frequency': [5, 10, 12, 15, 8, 20]
})

kmeans = KMeans(n_clusters=2)
df['segment'] = kmeans.fit_predict(df)

# Visualize
plt.scatter(df['amount_spent'], df['frequency'], c=df['segment'], cmap='rainbow')
plt.xlabel("Amount Spent")
plt.ylabel("Frequency")
plt.title("Customer Segments")
plt.show()
