# Write a function to print the even numbers from a given list. List is passed to the function as an argument.

def printEven(l):
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            print(l[i], end=" ")
        
printEven([1,7,4,9,6,11,2])