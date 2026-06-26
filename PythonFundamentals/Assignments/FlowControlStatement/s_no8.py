# Write a program to print the sum of all the digits of a given number.

n = int(input("Enter a number: "))
digit_sum = 0

while n > 0:
    digit_sum += int(n%10)
    n //= 10

print(digit_sum)
