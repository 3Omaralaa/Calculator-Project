import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
addition = add

def sub(n1, n2):
    return  n1 - n2
subtract = sub

def multi(n1, n2):
    return  n1 * n2
multiply = multi

def div(n1, n2):
    return  n1 / n2
divide = div

dictionary_operations = {
    "+": addition,
    "-": subtract,
    "*": multiply,
    "/": divide
 }

def calculator():
    first_num = int(input("What's the first number?: "))
    loop = True
    while loop:
        print('+\n-\n*\n/')
        pick = input("Pick an operation: ")
        second_num = int(input("What's the next number?: "))
        result = dictionary_operations[pick](first_num, second_num)
        print(f"{first_num} {pick} {second_num} = {result}")

        continue_working = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_working == "y":
            first_num = result
        else:
            loop = False
            calculator()

calculator()