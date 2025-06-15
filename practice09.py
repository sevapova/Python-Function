
def deposit(balance: float, amount: float) :
    '''Balansga mablag' qo'shadi
    
    Parametrlar:
        balance(float):Joriy balans.
        amount(float):qo'shiladigan summa

    Returns:
        float: Yangilangan balans.

    Scope:
        - Local: balance,amount
    
    '''
    return balance + amount

def withdraw(balance: float, amount: float) -> float :
    '''Balansdan mablag' yechadi, agar yetarli bo'lsa.

    Parametrlar:
        balance (float): Joriy balans.
        amount (float): Yechiladigan summa.

    Returns:
        float: Yangilangan balans yoki eski balans (yetarli bo'lmasa).

    Scope:
        - Local: balance, amount'''
    if amount > balance:
        print("Mablag' yetarli emas")
        return balance
    return balance - amount

def check_balance(balance: float) -> None:
    '''Joriy balansni chiqaradi.

    Parametr:
        balance (float): Balans miqdori.

    Returns:
        None

    Scope:
        - Local: balance'''
    print(balance)
    
def main() -> None :

    balance: float = 1200000
    print("deposit, withdraw,check_balance,exit")

    while True:
        x: str = input("Amalni kirit: ")
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


main()