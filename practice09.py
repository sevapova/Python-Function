
def deposit(balance, amount) :
    return balance + amount

def withdraw(balance, amount) :
    if amount > balance:
        print("Mablag' yetarli emas")
        return balance
    return balance - amount

def check_balance(balance) :
    print(balance)

balance = 1200000
print("deposit, withdraw,check_balance,exit")

while True:
    x = input("Amalni kirit: ")
    if x == "deposit":
        y = float(input("Summani kiriting: "))
        balance = deposit(balance,y)
    elif x == "withdraw":
        y = float(input("Summani kiriting: "))
        balance = withdraw(balance, y)
    elif x == "check":
        check_balance(balance)
    elif x == "exit":
        print("Xayr!")
        break
    else:
        print("Noto'g'ri amal")



