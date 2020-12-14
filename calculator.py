num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operation = input("Would you like to add/subtract/multiply/divide these numbers? ")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 // num2


if operation == "add":
    result = add(num1, num2)
    print(result)
elif operation == "subtract":
    result = subtract(num1, num2)
    print(result)
elif operation == "multiply":
    result = multiply(num1, num2)
    print(result)
elif operation == "divide":
    result = divide(num1, num2)
    print(result)