def is_palindrome(str_):
    str_new = "".join(str_.lower().split())  # TODO привести строку к единому регистру и избавиться от пробелов
    str_new = str_.lower()
    print(str_new)
    str_new = str_new.split()
    print(str_new)
    str_new = ''.join(str_new)
    print(str_new)




is_palindrome("Кит на море не романтик")