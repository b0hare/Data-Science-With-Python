# Write a function that takes a number as a parameter and checks whether the number is prime or not.

def isPrime(p):
    if p > 1:
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                return False
    else:
        return False
    return True

print(isPrime(33))