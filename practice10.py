

def is_strong_password(password: str) -> str:
    '''Parol kuchli yoki kuchsizligini tekshiradi.

    Shartlar:
    - Kamida 8 ta belgi
    - Faqat harf va raqamdan iborat bo'lishi (isalnum)

    Parametr:
        password (str): Tekshiriladigan parol.

    Returns:
        str: "Kuchli parol" yoki "Kuchsiz parol".

    Scope:
        - Local: password'''
    
    if password.isalnum() and len(password) >= 8 :
        print("Kuchli parol")
    else:
        print("Kuchsiz parol")

a = input("Parolni kiriting: ")
print(is_strong_password(a))


    
    