
def calculate_age(birth_year, current_year):
    age = current_year - birth_year

    if age < 0 :
        return "Sizning yiligingiz hozirgi yildan katta bo'lishi kerak. "
    
    if age >= 18 :
        x = "Siz balog'at yoshidasiz."

    else: 
        x = "Siz balog'at yoshida emassiz."

    return f"Sizning yoshingiz {age} yosh . {x}"

y = calculate_age(2005,2025)
print(y)
