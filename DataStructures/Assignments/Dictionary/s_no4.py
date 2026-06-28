# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

d = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Bhopal"
}

print("\nKeys:")
for key in d.keys():
    print(key)

print("\nValues:")
for value in d.values():
    print(value)

print("\nKeys and Values:")
for key, value in d.items():
    print(key, ":", value)

print("\n")