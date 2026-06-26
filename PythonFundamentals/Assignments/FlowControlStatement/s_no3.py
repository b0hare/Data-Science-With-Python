# problem 
# Given two non-negative values, print true if they have the same last digit.

def lastDigit(n1, n2):
    if n1 % 10 == n2 % 10:
        return True
    return False

print(lastDigit(47,404))