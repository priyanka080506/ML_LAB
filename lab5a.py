import matplotlib.pyplot as plt

n = int(input("Enter number of leaf nodes: "))
values = list(map(int, input("Enter values: ").split()))

best = max(values)

print("Optimal Value:", best)

plt.bar(range(len(values)), values)
plt.axhline(y=best, linestyle='--')
plt.title("Min-Max Algorithm")
plt.xlabel("Leaf Nodes")
plt.ylabel("Values")
plt.show()
