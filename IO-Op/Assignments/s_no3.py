# Write a program to accept input from user and append it to a txt file.

s = str(input("Enter the input: "))
f = open('file.txt', 'w')
print(f.write(s))

f.close()