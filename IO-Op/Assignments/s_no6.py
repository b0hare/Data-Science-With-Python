# Write a program to count the frequency of a user entered word in a txt file.

word = str(input("Enter a word to count frequency: "))

file = open("file.txt", 'r')

text = file.read().lower()

words = text.split()

count = 0

for w in words:
    if w == word:
        count+= 1

print("Frequency of '%s' is %d" % (word, count))