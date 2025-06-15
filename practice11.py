def calculate_tax(salary: float) -> float :
    '''Berilgan maoshga qarab soliqni hisoblaydi.

    - Agar maosh > 5,000,000 bo‘lsa → 20%
    - Aks holda → 13%

    Parametr:
        salary (float): Foydalanuvchi maoshi.

    Returns:
        float: Hisoblangan soliq miqdori.

    Scope:
        - Local: salary'''
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary: float) -> float:
    ''' Soliqdan so'ng qoladigan sof maoshni hisoblaydi.

    Parametr:
        salary (float): Umumiy maosh.

    Returns:
        float: Sof maosh (soliqdan keyin qolgan).

    Scope:
        - Local: salary, tax'''
    tax = calculate_tax(salary)
    return salary - tax

x = input("Maoshingizni kiriting: ")
y = float(x)

a = calculate_tax(x)
b = calculate_net_salary(x)

print(a)
print(b)