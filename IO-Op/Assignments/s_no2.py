# Write a program to read first n lines from a txt file. Get n as user input.

f1 = open('file.txt')

n = int(input("\nEnter no of line to read from file: "))

while n > 0:
    print(f1.readline())
    n-=1
    
f1.close()
print()