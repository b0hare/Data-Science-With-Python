def isPalindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

def count_the_vowels(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] in "aeiou":
            count += 1
    return count

def freq_of_letters(s):
    l = [0]*26
    s = s.upper()
    
    for i in range(len(s)):
        char = s[i]
        if 'A' <= char <= 'Z':
            l[ord(char) - 65] += 1
            
    for i in range(len(l)):
        if l[i] > 0:
            print(f"{chr(i + 65)}: {l[i]}", end=", ")
    print("\n")
    