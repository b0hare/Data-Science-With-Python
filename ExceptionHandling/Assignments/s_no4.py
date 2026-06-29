# Declare a list with 10 integers and ask the user to enter an index. Check whether the number at that index is positive or negative. If any invalid index is entered, handle the exception and print an error message.

numbers = [12, -5, 18, -9, 7, -14, 25, -30, 40, -2]

try:
    index = int(input("Enter index (0-9): "))

    value = numbers[index]

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer index.")

except Exception as e:
    print("Error:", e)

else:
    if value >= 0:
        print(value, "is a Positive Number")
    else:
        print(value, "is a Negative Number")