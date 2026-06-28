# Write a program to accept two numbers as command line arguments and display their sum.


from sys import argv

n1 = argv[1]
n2 = argv[2]

sum = int(n1)+ int(n2)
print(sum)
