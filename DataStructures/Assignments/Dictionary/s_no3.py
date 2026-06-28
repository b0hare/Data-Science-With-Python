# Write a program to check if a given key already exists in a dictionary.

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = int(input("\nEnter key: "))

if key in dict1.keys():
    print("Key already exist!\n")
else:
    print("No key found!\n")
