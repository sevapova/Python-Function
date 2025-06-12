

def is_even(number):
    return number % 2 == 0 

def print_even_message(number):

    if is_even(number):
        print(f"{number} juft son")
    
    else:
        print(f"{number} toq son")
            
print(is_even(4))
print_even_message(4)
print_even_message(9)
