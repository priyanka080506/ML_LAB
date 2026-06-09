from queue import PriorityQueue
import matplotlib.pyplot as plt

n = int(input("Enter number of nodes: "))

pq = PriorityQueue()
visited = []
y = []

for i in range(n):
    node = input("Enter node: ")
    h = int(input("Enter heuristic value: "))
    pq.put((h, node))

step = 1
while not pq.empty():
    h, node = pq.get()
    visited.append(node)
    y.append(step)
    step += 1

print("Traversal Order:", visited)

plt.plot(visited, y, marker='o')
plt.title("Best First Search")
plt.xlabel("Nodes")
plt.ylabel("Visit Order")
plt.grid()
plt.show()
