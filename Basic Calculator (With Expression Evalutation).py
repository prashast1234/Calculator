def calculator():
    print("Simple Calculator")
    print("Type expressions like 2+3, 5*6-2, 10/2+7, etc.")
    print("Type 'q' to quit.\n")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == "q":
            print("Calculator closed.")
            break

        try:
            # eval evaluates full math expressions
            result = eval(expression)
            print("Result:", result)
        except:
            print("Invalid input, please retry.")

calculator()