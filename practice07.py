
def check_answer(user_answer: str, correct_answer: str) -> str:
    '''Foydalanuvchining javobini to'g'riligi bo'yicha tekshiradi.

        Parametrlar:
            user_answer (str): Foydalanuvchi kiritgan javob.
            correct_answer (str): To'g'ri javob.

        Returns:
            str: To'g'ri yoki xato degan xabar.

        Scope:
            - Local: user_answer, correct_answer'''
    if user_answer.strip().upper() == correct_answer.strip().upper() :
        print("Javob to'g'ri malades")
    else:
        print("Sizning javobingiz xato")

correct_answer = "Samarqand"
user_answer = input("O'zbekiston poytaxti nima? ")

a = check_answer(user_answer,correct_answer)
print(a)