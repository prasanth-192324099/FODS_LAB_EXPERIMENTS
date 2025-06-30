import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = {'age': [23, 45, 34, 50, 41, 35, 30, 27, 49, 37, 38, 40, 42, 29, 33, 36, 43, 44],
        'fat_percent': [18, 25, 20, 28, 23, 21, 19, 17, 26, 22, 24, 25, 27, 19, 20, 21, 23, 24]}
df = pd.DataFrame(data)

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Std Dev:\n", df.std())

# Boxplots
df[['age', 'fat_percent']].plot(kind='box')
plt.title("Boxplot of Age and %Fat")
plt.show()

# Scatter and Q-Q plot
sns.scatterplot(data=df, x='age', y='fat_percent')
plt.title("Scatter Plot")
plt.show()

stats.probplot(df['fat_percent'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Fat %")
plt.show()