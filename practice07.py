
def check_answer(user_answer, correct_answer) :

    if user_answer.strip().upper() == correct_answer.strip().upper() :
        print("Javob to'g'ri malades")
    else:
        print("Sizning javobingiz xato")

correct_answer = "Samarqand"
user_answer = input("O'zbekiston poytaxti nima? ")

a = check_answer(user_answer,correct_answer)
print(a)