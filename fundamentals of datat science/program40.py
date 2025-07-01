import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    'name': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6'],
    'age': [22, 30, 25, 28, 24, 29],
    'position': ['Forward', 'Midfielder', 'Defender', 'Forward', 'Defender', 'Goalkeeper'],
    'goals': [10, 5, 2, 12, 1, 0],
    'salary': [20000, 25000, 22000, 30000, 21000, 18000]
})

# Top 5 by goals and salary
top_goals = df.nlargest(5, 'goals')[['name', 'goals']]
top_salary = df.nlargest(5, 'salary')[['name', 'salary']]
print("Top 5 Goal Scorers:\n", top_goals)
print("\nTop 5 Salaries:\n", top_salary)

# Average age
avg_age = df['age'].mean()
above_avg = df[df['age'] > avg_age]
print("\nPlayers above average age:\n", above_avg[['name', 'age']])

# Position distribution
df['position'].value_counts().plot(kind='bar', title='Player Position Distribution')
plt.xlabel("Position")
plt.ylabel("Count")
plt.show()