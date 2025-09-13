print("Enter the prompt. Type '*' to multiply, '/' to divide, '+' to add, and '-' to subtract")

def calculator():
    call = input("Enter operation: ")

    if call == "*":
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: ")) 
        print("Result:", number1 * number2)

    elif call == "/":
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: ")) 
        print("Result:", number1 / number2)

    elif call == "+":
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: ")) 
        print("Result:", number1 + number2)

    elif call == "-":
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: ")) 
        print("Result:", number1 - number2)

    else:
        print("Invalid input, please retry")

calculator()