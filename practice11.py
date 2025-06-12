def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax

x = input("Maoshingizni kiriting: ")
y = float(x)

a = calculate_tax(x)
b = calculate_net_salary(x)

print(a)
print(b)
