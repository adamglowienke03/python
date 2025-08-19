def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    first_number = float(input("What is your first number? "))

    while True:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        second_number = float(input("What is your next number? "))
        result = round(operations[operation](first_number, second_number), 2)
        print(f"{first_number} {operation} {second_number} = {result}")
        is_continue = input(f"Is it continue with a {result}? (y/n): ")
        if is_continue == "y":
            first_number = result
        else:
            print("\n" * 10)
            calculator()

calculator()
