from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

features = [5.1, 3.5, 1.4, 0.2]
# features = [float(input(f"{name}: ")) for name in iris.feature_names]

prediction = clf.predict([features])
print("Predicted species:", iris.target_names[prediction[0]])
