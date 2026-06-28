
# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

from sys import argv

print(argv[0], "says", argv[1])