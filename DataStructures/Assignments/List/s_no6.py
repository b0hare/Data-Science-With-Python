# Write a program to insert a new item before the second element in an existing list.

my_list = [10, 20, 30, 40]

print("\nlist is: ", my_list)
item = int(input("\nEnter the item to insert: "))

my_list.insert(1, item)

print("Updated List: ", my_list, "\n")