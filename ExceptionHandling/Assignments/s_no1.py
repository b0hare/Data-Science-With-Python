# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Error:", e)

else:
    print("Result =", result)