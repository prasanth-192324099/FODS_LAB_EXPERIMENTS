import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df = pd.DataFrame({
    'age': [25, 35, 45, 30, 50, 28, 38, 48, 33, 55],
    'bp': [120, 140, 130, 135, 145, 118, 142, 128, 134, 150],
    'chol': [180, 210, 200, 195, 220, 175, 215, 198, 192, 225],
    'outcome': ['Good', 'Bad', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Bad', 'Good', 'Bad']
})

X = df[['age', 'bp', 'chol']]
y = df['outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted:", list(y_pred))
print("Actual   :", list(y_test))

print(classification_report(y_test, y_pred, zero_division=1))
