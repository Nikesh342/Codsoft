# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

    num1 = float(input("Enter the first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif operation == '-':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '*':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '/':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation! Please use +, -, *, or /.")

# Run the calculator
calculator()
