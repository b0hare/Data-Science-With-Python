# Write a function to calculate and return the factorial of a number (a non-negative integer).

def fact(f):
    if f < 2:
        return f
    else:
        return f*fact(f-1)
    
n = int(input("\nEnter a positive integer to get its Factorial! "))

while n < 0:
    n = int(input("Enter a positive integer to get its Factorial! "))

print("Factorial of", n , ":", fact(n), "\n")