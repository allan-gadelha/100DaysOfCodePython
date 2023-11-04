from calculator_art import logo

print(logo)

def add(n1, n2):
    """This function sum the first and second number"""
    return n1 + n2

def subtract(n1,n2):
    """This function subtracts the first and second number"""
    return n1 - n2

def multiply(n1, n2):
    """This function multiply the first and second number"""
    return n1 * n2

def divide(n1, n2):
    """This function divide the first number by the second number"""

def calculation(n1, n2, operation_order):
    if operation_order == "+":
        return n1 + n2
    elif operation_order == "-":
        return n1 - n2
    elif operation_order == "*":
        return n1-n2

first_number = int(input("What's the first number?: "))

operation = input("+\n-\n*\n/\nPick a operation: ")

second_number = int(input("What's the next number?: "))

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}