def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_status(bmi):
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
