

def check_guess(secret: int, guess: int) -> bool:
    return secret == guess
'''Foydalanuvchi kiritgan son kompyuter soniga tengligini tekshiradi.

    Parametrlar:
        secret (int): Kompyuter tanlagan son.
        guess (int): Foydalanuvchi taxmin qilgan son.

    Returns:
        bool: True — agar sonlar teng bo'lsa, False — aks holda.

    Scope:
        - Local: secret, guess'''

def print_result(is_correct: bool) -> None :
    '''Natijani foydalanuvchiga chiqaradi.

    Parametr:
        is_correct (bool): Foydalanuvchining javobi to‘g‘rimi yoki yo‘qmi.

    Scope:
        - Local: is_correct'''
    
    if is_correct :
        print("To'g'ri topdingiz malades!")

    else:
        print("Xato")
def main() -> None :
    '''Asosiy funksiya: kompyuter soni va foydalanuvchi sonini solishtiradi,
    natijani chiqaradi.

    Scope:
        - Local: num1, num2, result
    '''
    num1 = int(input("Kompyuter kiritgan son: "))
    num2 = int(input("Sonni kiriting: "))
    result = check_guess(num1,num2)
    print_result(result)

main()