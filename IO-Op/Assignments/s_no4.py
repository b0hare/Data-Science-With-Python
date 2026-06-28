# Write a program to read contents from a txt file line by line and store each line into a list.

file = open('file.txt')

lines = []

for line in file:
    lines.append(line.strip())
    
file.close()
print(lines)

