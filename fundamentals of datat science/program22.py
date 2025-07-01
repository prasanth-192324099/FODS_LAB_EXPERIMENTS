import pandas as pd
import scipy.stats as stats

df = pd.read_csv("customer_reviews.csv")
df.columns = df.columns.str.strip().str.lower()
print("Cleaned Columns:", df.columns.tolist())

ratings = df['rating'].dropna()

mean = ratings.mean()
sem = stats.sem(ratings)
ci_95 = stats.t.interval(0.95, df=len(ratings)-1, loc=mean, scale=sem)

print("Mean Rating:", round(mean, 2))
print("SEM:", round(sem, 4))
print("95% Confidence Interval:", (round(ci_95[0], 2), round(ci_95[1], 2)))
