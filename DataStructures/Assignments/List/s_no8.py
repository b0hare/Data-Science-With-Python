# Write a program to remove the first occurrence of a specified element from a list.


my_list = [10, 20, 30, 20, 40]

print("\nlist is: ", my_list)

item = int(input("\nEnter the element to remove: "))

my_list.remove(item)

print("Updated List: ", my_list, "\n")