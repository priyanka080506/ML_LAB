from queue import PriorityQueue
import matplotlib.pyplot as plt

n = int(input("Enter number of nodes: "))

pq = PriorityQueue()
nodes = []
f_values = []

for i in range(n):
    node = input("Enter node: ")
    g = int(input("Enter g(n): "))
    h = int(input("Enter h(n): "))

    f = g + h
    pq.put((f, node))

while not pq.empty():
    f, node = pq.get()
    nodes.append(node)
    f_values.append(f)

print("A* Order:", nodes)

plt.plot(nodes, f_values, marker='o')
plt.title("A* Algorithm")
plt.xlabel("Nodes")
plt.ylabel("f(n)=g(n)+h(n)")
plt.grid()
plt.show()
