# Write a program to accept a number from the user and check whether it's prime or not. If the user enters anything other than a number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))

    if num < 2:
        print("Not a Prime Number")
    else:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime Number")
        else:
            print("Not a Prime Number")

except ValueError:
    print("Error: Please enter a valid integer.")