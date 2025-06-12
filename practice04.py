
def get_grade(score) :
    if score < 0 or score > 100 :
        return "Noto'g'ri ball kiritdingiz!"
    elif score >= 90:
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    else:
        return "F"
    
a = int(input("Ballingizni kiriting: "))
b = get_grade(a)
print(f"Sizning bahongiz: {b}")

