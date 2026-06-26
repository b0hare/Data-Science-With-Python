"""Write a program to find if the given number is a palindrome or not.

Example 1:

Input: 110011
Output: 110011 is a palindrome.

Example 2:

Input: 1234
Output: 1234 is not a palindrome."""

n = int(input("Enter a number: "))

s = str(n)
isPalindrome = True

start = 0
end = len(s) - 1

while start < end:
    if(s[start] != s[end]):
        isPalindrome = False
        break
    start+=1
    end-=1
    
print(isPalindrome)