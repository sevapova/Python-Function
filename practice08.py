
def c_to_f(celsius):
   return celsius *9/5 + 32

def f_to_c(fahrenheit):
   return (fahrenheit - 32) * 5/9

celsius = float(input("Sonni kiriting: "))
fahrenheit = c_to_f(celsius)

print(fahrenheit)
