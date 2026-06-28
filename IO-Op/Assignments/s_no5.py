# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

file = open("file.txt", "r")

text = file.read()

file.close()

words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)