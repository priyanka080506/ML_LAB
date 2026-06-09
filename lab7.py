import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

file = input("Enter dataset file (glass.csv / fruit.csv): ")

data = pd.read_csv(file)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

results = []

for split in [0.1, 0.3]:      # 90-10 and 70-30
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=split, random_state=42)

    for k in [3, 5, 7]:

        # Euclidean Distance
        knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
        knn.fit(X_train, y_train)
        pred = knn.predict(X_test)
        acc = accuracy_score(y_test, pred) * 100

        print(f"Split={int((1-split)*100)}-{int(split*100)}, "
              f"K={k}, Euclidean Accuracy={acc:.2f}")

        results.append(acc)

        # Manhattan Distance
        knn = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
        knn.fit(X_train, y_train)
        pred = knn.predict(X_test)
        acc = accuracy_score(y_test, pred) * 100

        print(f"Split={int((1-split)*100)}-{int(split*100)}, "
              f"K={k}, Manhattan Accuracy={acc:.2f}")

        results.append(acc)

labels = [
    "3-E","3-M","5-E","5-M","7-E","7-M",
    "3-E","3-M","5-E","5-M","7-E","7-M"
]

plt.figure(figsize=(8,4))
plt.bar(labels, results)
plt.title("KNN Accuracy Comparison")
plt.xlabel("K and Distance Metric")
plt.ylabel("Accuracy (%)")
plt.show()
