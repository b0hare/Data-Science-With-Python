# Write a program to find the index of an item in a tuple.


t = (10, 20, 30, 40, 50)

item = int(input("Enter the element: "))

index = t.index(item)

print("Index of", item, "is", index)