import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'amount_spent': [100, 500, 300, 800, 200, 1000],
    'items_purchased': [2, 6, 3, 8, 2, 10]
})

kmeans = KMeans(n_clusters=2)
df['segment'] = kmeans.fit_predict(df)

plt.scatter(df['amount_spent'], df['items_purchased'], c=df['segment'], cmap='Accent')
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Clustering")
plt.show()