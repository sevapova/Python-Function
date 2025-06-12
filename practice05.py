

def check_guess(secret, guess) :
    return secret == guess

def print_result(is_correct) :
    
    if is_correct :
        print("To'g'ri topdingiz malades!")

    else:
        print("Xato")

num1 = int(input("Kompyuter kiritgan son: "))
num2 = int(input("Sonni kiriting: "))
result = check_guess(num1,num2)

print_result(result)
