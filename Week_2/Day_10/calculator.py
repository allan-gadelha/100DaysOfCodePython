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
    if n2 == 0:
        return "Error: Division by zero"
    else:
        return n1 / n2

#Creating a recursion to make the program flow better
def calculator():

    #Asking the user for the first number
    first_number = float(input("What's the first number?: "))

    #Dictionarie to save operation with respective function, really nice way to save functions for a keyword!
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }

    #Printing operation for user to see the possibles ones
    for symbol in operations:
        print(symbol)

    #Loop to keep going till the user don't want anymore
    should_continue = True
    while should_continue:
        
        #Picking the operation in each iteration
        operation_symbol = input("Pick a operation: ")

        #If operation does not exist in operations give a feedback for the user, and make him try again!
        if operation_symbol not in operations:
            print("Invalid Operation")
        else:
            #If operation exist keep going and ask about the second number
            second_number = float(input("What's the second number?: "))

            #Creating a new variable that will get the function from the operations! So calculation_function becomes the function!!
            calculation_function = operations[operation_symbol]

            #Creating the answer!
            answer = calculation_function(first_number, second_number)

            #Printing the complete calculation
            print(f"{first_number} {operation_symbol} {second_number} = {answer}")

            #Asking if the user still wants to keep calculating
            keep_calculating = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
            
            if keep_calculating == "y":
                first_number = answer
            elif keep_calculating == "n":
                should_continue = False
                calculator()

calculator()