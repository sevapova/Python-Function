
def is_valid_phone_number(phone: str):

    if phone.isdigit() and len(phone) == 9:
        return "Raqam to'g'ri kiritildi"
    else:
        return "Raqam xato kiritildi."

    
a = (input("Raqamni kiriting: "))
print(is_valid_phone_number(a))