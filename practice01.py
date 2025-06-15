def add(a: int , b: int) -> int :
    return a + b
'''Qo'shish funksiyasi.

    Parametrlar:
        a (int): Birinchi son.
        b (int): Ikkinchi son.

    Returns:
        int: a + b qiymati.

    Scope:
        - Local: a, b (faqat shu funksiyada ishlaydi)'''

def subtract(a: int, b: int ) -> int :
    return a - b
'''Ayirish funksiyasi.

    Parametrlar:
        a (int): Birinchi son.
        b (int): Ikkinchi son.

    Returns:
        int: a - b qiymati.

    Scope:
        - Local: a, b (faqat shu funksiyada ishlaydi)'''

def multiply(a: int, b: int)  -> int :
    return a * b
'''Ko'patirish funksiyasi.

    Parametrlar:
        a (int): Birinchi son.
        b (int): Ikkinchi son.

    Returns:
        int: a * b qiymati.

    Scope:
        - Local: a, b (faqat shu funksiyada ishlaydi)'''

def divide(a: int, b: int) -> float :
    return a / b
'''Bo'lish funksiyasi.

    Parametrlar:
        a (int): Birinchi son.
        b (int): Ikkinchi son.

    Returns:
        int: a / b qiymati.

    Scope:
        - Local: a, b (faqat shu funksiyada ishlaydi)'''
def main () :
    '''Asosiy funksiya.

    Foydalanuvchidan ikkita son va matematik operator (+, -, *, /) oladi.
    Mos funksiyani chaqiradi va natijani chiqaradi.

    Scope:
        - Local: a, b, operator (faqat shu funksiyada mavjud)
    '''
    a = int(input("a = "))
    operator = input("(+, -, *,/) = ")
    b = int(input("b = "))
    
    if operator == "+":
        print(add(a,b))

    elif operator == "-":
        print(subtract(a,b))

    elif operator == "*":
        print(multiply(a,b))

    elif operator == "/":
        if b == 0 :
            print("0 bo'lishi mumkin emas")
        else:
            print(divide(a,b))

    else :
        print("Bunday operator yo'q")
    main()

main()