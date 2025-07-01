import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    'purchase_amount': [200, 500, 800, 150, 1200, 700, 300],
    'visit_frequency': [3, 5, 8, 2, 10, 6, 4]
})

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df)

# Visualize
plt.scatter(df['purchase_amount'], df['visit_frequency'], c=df['cluster'], cmap='viridis')
plt.xlabel("Purchase Amount")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation")
plt.show()
