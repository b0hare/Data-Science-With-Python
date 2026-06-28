students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

print("\nStudents list is: ", students)
name = input("Enter a name: ")

average = sum(students[name]) / len(students[name])

print("Average percentage mark:", average, "\n")