import matplotlib.pyplot as plt

arr = list(map(int, input("Enter values: ").split()))

current = arr[0]
path = [current]

for x in arr[1:]:
    if x > current:
        current = x
        path.append(current)

print("Best Solution:", current)

plt.plot(path, marker='o')
plt.title("Hill Climbing")
plt.xlabel("Step")
plt.ylabel("Value")
plt.show()
