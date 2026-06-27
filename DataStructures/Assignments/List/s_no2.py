# Write a program to append a new item to the end of the list.

my_list = [1,3,5,9,12]

print("\nList before Append: ")
for i in range(0, len(my_list)):
    print(my_list[i], end="\t")
    
item = int(input("\n\nEnter an integer: "))

print("\nList After Appending ", item)

my_list.append(item)

for i in range(0, len(my_list)):
    print(my_list[i], end="\t")