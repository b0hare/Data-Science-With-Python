# Write a program to sum all the values in a dictionary, considering the values will be of int type.

d = {
    "Math": 80,
    "Science": 90,
    "English": 85
}

print("\nValues:")
for value in d.values():
    print(value, end="\t")

total = sum(d.values())

print("\nSum of all values:", total, "\n")