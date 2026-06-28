# Write a program that will check whether a given String is Palindrome or not.

string = input("Enter a string: ")

string = string.lower()

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")