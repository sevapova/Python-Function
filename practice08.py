
def c_to_f(celsius: float) -> float :
    '''Selsiy darajasini Farengeytga aylantiradi.

    Parametr:
        celsius (float): Selsiy darajasi.

    Returns:
        float: Farengeyt darajasi.

    Scope:
        - Local: celsius'''
   
    return celsius *9/5 + 32

def f_to_c(fahrenheit):
   return (fahrenheit - 32) * 5/9

celsius = float(input("Sonni kiriting: "))
fahrenheit = c_to_f(celsius)

print(fahrenheit)