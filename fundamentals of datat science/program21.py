import pandas as pd
import numpy as np
import scipy.stats as stats

# Load data
df = pd.read_csv("rare_elements.csv")  # one column with measurements

sample_size = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g., 0.95): "))

sample = df.sample(sample_size).iloc[:, 0]
mean = sample.mean()
sem = stats.sem(sample)
margin = sem * stats.t.ppf((1 + confidence) / 2, sample_size - 1)

print(f"{int(confidence*100)}% Confidence Interval: ({mean - margin:.2f}, {mean + margin:.2f})") 