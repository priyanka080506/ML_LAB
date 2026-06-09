import matplotlib.pyplot as plt

n = int(input("Enter number of leaf nodes: "))
values = list(map(int, input("Enter values: ").split()))

alpha = max(values)
visited = values[:-1]  # assume last node pruned

print("Best Value:", alpha)

plt.bar(range(len(visited)), visited)
plt.title("Alpha-Beta Pruning")
plt.xlabel("Visited Nodes")
plt.ylabel("Values")
plt.show()
