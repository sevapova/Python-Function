
def is_valid_phone_number(phone: str) -> str:
    '''Telefon raqamini tekshiruvchi funksiya.

    Raqam faqat raqamlardan iborat bo'lishi va uzunligi 9 bo'lishi kerak.

    Parametr:
        phone (str): Tekshirilayotgan telefon raqami.

    Returns:
        str: "Raqam to'g'ri kiritildi" yoki "Raqam xato kiritildi."

    Scope:
        - Local: phone'''

    if phone.isdigit() and len(phone) == 9:
        return "Raqam to'g'ri kiritildi"
    else:
        return "Raqam xato kiritildi."

    
a = (input("Raqamni kiriting: "))
print(is_valid_phone_number(a))