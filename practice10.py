

def is_strong_password(password) :
    
    if password.isalnum() and len(password) >= 8 :
        print("Kuchli parol")
    else:
        ("Kuchsiz parol")

a = input("Parolni kiriting: ")
print(is_strong_password(a))


    
    