# Write a program to remove the item from a specified index in a list.

my_list = [10, 20, 30, 40, 50]

print("\nlist is: ", my_list)

index = int(input("Enter the index to remove: "))

my_list.pop(index)

print("Updated List: ", my_list, "\n")