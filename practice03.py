

def is_even(number: int) -> bool :
    return number % 2 == 0 
'''Sonning juft yoki toqligini aniqlash funksiyasi.

    Parametrlar:
        number (int): Tekshiriladigan son.

    Returns:
        bool: True, agar son juft bo'lsa, aks holda False.

    Scope:
        - Local: number (faqat shu funksiyada ishlaydi)'''

def print_even_message(number: int) -> None :
    '''Son haqida xabar chiqarish funksiyasi.
    
    Agar son juft bo'lsa, "juft son" deb, aks holda "toq son" deb chiqaradi.

    Parametrlar:
        number (int): Natijasi chiqariladigan son.

    Scope:
        - Local: number'''

    if is_even(number):
        print(f"{number} juft son")
    
    else:
        print(f"{number} toq son")
            
print(is_even(4))
print_even_message(4)
print_even_message(9)