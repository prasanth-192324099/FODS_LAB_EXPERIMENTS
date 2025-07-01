
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'study_time': [1, 2, 3, 4, 5, 6, 7],
    'exam_score': [55, 60, 65, 70, 75, 80, 90]
})

correlation = df.corr()
print("Correlation Matrix:\n", correlation)

sns.regplot(x='study_time', y='exam_score', data=df)
plt.title("Study Time vs Exam Score")
plt.show()
