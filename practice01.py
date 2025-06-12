def add(a,b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b 
    return result

def divide(a, b):
    result = a / b
    return result

def main():
    a = int(input("a = "))
    operator = input("(+, -, *, /) = ")
    b = int(input("b = "))

    if operator == "+":
       print(add(a,b))

    elif operator == "-":
        print(subtract(a,b))

    elif operator == "*":
        print(multiply(a,b))

    elif operator == "/":
        print(divide(a,b))

    else:
        print("Bunday operator yo'q")

main()