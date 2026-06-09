data = []

while True:
    print("\n1.Insert 2.Update 3.Delete 4.Display 5.Sort 6.Search 7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        data.append(input("Enter item: "))

    elif ch == 2:
        old = input("Item to update: ")
        if old in data:
            data[data.index(old)] = input("New item: ")

    elif ch == 3:
        item = input("Item to delete: ")
        if item in data:
            data.remove(item)

    elif ch == 4:
        print(data)

    elif ch == 5:
        data.sort()
        print("Sorted:", data)

    elif ch == 6:
        item = input("Item to search: ")
        if item in data:
            print("Found")
        else:
            print("Not Found")

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
