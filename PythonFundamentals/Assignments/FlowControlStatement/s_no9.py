""" Write a program to reverse a given number and print it.

Example 1:

Input: 1234
Output: 4321

Example 2:

Input: 1004
Output: 4001 """


n = int(input("Enter a number: "))

s = str(n)

print(int(s[::-1]))