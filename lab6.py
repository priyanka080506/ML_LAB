import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

model = GaussianNB()

# ---------- IRIS DATASET ----------
iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)
model.fit(X_train, y_train)
iris_90 = accuracy_score(y_test, model.predict(X_test)) * 100

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
iris_70 = accuracy_score(y_test, model.predict(X_test)) * 100

# ---------- TITANIC DATASET ----------
data = pd.read_csv("titanic.csv")

data = data[['Pclass', 'Sex', 'Age', 'Survived']]
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = data.dropna()

X = data[['Pclass', 'Sex', 'Age']]
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)
model.fit(X_train, y_train)
titanic_90 = accuracy_score(y_test, model.predict(X_test)) * 100

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
titanic_70 = accuracy_score(y_test, model.predict(X_test)) * 100

print("Iris 90-10 Accuracy =", iris_90)
print("Iris 70-30 Accuracy =", iris_70)
print("Titanic 90-10 Accuracy =", titanic_90)
print("Titanic 70-30 Accuracy =", titanic_70)

# ---------- PLOT ----------
labels = ['Iris 90-10', 'Iris 70-30',
          'Titanic 90-10', 'Titanic 70-30']
accuracy = [iris_90, iris_70, titanic_90, titanic_70]

plt.bar(labels, accuracy)
plt.title("Naive Bayes Accuracy Comparison")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=15)
plt.show()
