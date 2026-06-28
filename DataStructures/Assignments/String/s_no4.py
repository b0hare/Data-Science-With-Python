# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".


string = input("Enter a string: ")

if string.startswith('x'):
    string = string[1:]

if string.endswith('x'):
    string = string[:-1]

print("Output:", string)