
def calculate_bmi(weight: float, height: float) -> float :
    '''BMI (tana massasi indeksi) ni hisoblaydi.

    Formula:
        BMI = weight / (height^2)

    Parametrlar:
        weight (float): Og'irlik (kg).
        height (float): Bo'y uzunligi (m).

    Returns:
        float: BMI qiymati.

    Scope:
        - Local: weight, height'''

    return weight / (height ** 2)

def bmi_status(bmi: float) -> str :
    ''' BMI qiymatiga asoslangan sog‘liq holatini qaytaradi.

    Parametr:
        bmi (float): BMI qiymati.

    Returns:
        str: Holat ("Ozgin", "Normal", "Semiz", "Juda semiz").

    Scope:
        - Local: bmi'''
    if bmi < 18.5:
        return "Ozgin"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Semiz"
    else:
        return "Juda semiz"

a = float(input("Og'rlikni kiriting (kg): "))
b = float(input("Bo'yni kiriting (m): "))

bmi = calculate_bmi(a,b)
status = bmi_status(bmi)

print(round(bmi, 2))
print(status)