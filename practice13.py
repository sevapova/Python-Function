
def is_palindrome(text: str) -> bool :
    return text == text[::-1]

a = input("So'zni kiriting: ")

if is_palindrome(a):
    print("Bu so'z palinom ")

else :
    print("Bu so'z palinom emas!")



