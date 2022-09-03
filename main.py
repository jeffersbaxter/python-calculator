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
    "/": divide
}

num1 = int(input("What's the first number?: "))

answer = "Couldn't perform operation"
performing_operations = True
while performing_operations:
    op = input("What operation should we perform?: '+', '-', '*', '/' ")
    while not op in operations:
        op = input("Operation not valid. Try again: '+', '-', '*', '/' ")

    num2 = int(input("What's the second number?: "))

    answer = operations[op](num1, num2)

    print(f"{num1} {op} {num2} = {answer}")
    run_again = input("Would you like to perform another operation? 'y' or 'n' ")
    if run_again == 'n':
        performing_operations = False
    else:
        num1 = answer

print(f"{num1} {op} {num2} = {answer}")

