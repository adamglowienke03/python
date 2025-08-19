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

first_number = float(input("What is your first number? "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
second_number = float(input("What is your second number? "))
result = round(operations[operation](first_number, second_number), 2)
print(f"{first_number} {operation} {second_number} = {result}")

while True:
    is_continue = input("Is it continue with a result? (y/n): ")
    if is_continue == "y":
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_number = float(input("What is your next number? "))
        new_result = round(operations[operation](result, second_number), 2)
        print(f"{result} {operation} {second_number} = {new_result}")
        result = new_result
    else:
        break
