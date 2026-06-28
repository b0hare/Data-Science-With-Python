# Write a program to check whether an element exists in a tuple or not.

t = (10, 20, 30, 40, 50)

item = int(input("Enter the element to search: "))

if item in t:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")