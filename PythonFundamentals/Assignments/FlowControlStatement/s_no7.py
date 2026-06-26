# Write a program to print prime numbers between 10 and 99.

for i in range(10, 100):
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
    if(isPrime):
        print(i, end="\t")