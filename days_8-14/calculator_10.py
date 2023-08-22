# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    num1 = float(input("What is the first number?\n"))
    print("Select the operation you want: ")
    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operation_sign = input("Pick an operation: ")
        num2 = float(input("What is the next number?\n"))
        answer = operations[operation_sign](num1, num2)
        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculations with {answer}, or 'n' to start new calcul: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
