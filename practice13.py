
def is_palindrome(text: str) -> bool :
    ''' Berilgan matn palindrom ekanligini tekshiradi.

    Palindrom — o'qishda chapdan ham, o'ngdan ham bir xil bo‘lgan so‘z yoki ibora.

    Parametr:
        text (str): Tekshiriladigan so'z yoki matn.

    Returns:
        bool: True — agar palindrom bo'lsa, aks holda False.

    Scope:
        - Local: text'''
    return text == text[::-1]

def main() -> None :

    a: str = input("So'zni kiriting: ")

    if is_palindrome(a):
        print("Bu so'z palinom ")

    else :
        print("Bu so'z palinom emas!")

main()
