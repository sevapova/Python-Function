
def calculate_age(birth_year: int, current_year: int) -> str :
    '''Foydalanuvchining tug'ilgan yili va hozirgi yil asosida yoshini hisoblaydi.
    
    Args:
        birth_year (int): Tug'ilgan yil
        current_year (int): Hozirgi yil
    
    Returns:
        str: Foydalanuvchining yoshi va balog'atga yetganligi haqida xabar'''
    age = current_year - birth_year

    if age < 0 :
        return "Sizning yiligingiz hozirgi yildan katta bo'lishi kerak. "
    
    if age >= 18 :
        x = "Siz balog'at yoshidasiz."

    else: 
        x = "Siz balog'at yoshida emassiz."

    return f"Sizning yoshingiz {age} yosh . {x}"

a: str = calculate_age(2005,2025)
print(a)
