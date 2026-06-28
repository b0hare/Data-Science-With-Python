# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

from sys import argv

sum = 0

for i in range(1, len(argv)):
    sum += int(argv[i])
    
print("Sum is", sum)