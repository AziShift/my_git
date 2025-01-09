string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")


if len(string1) > len(string2):
    print("Первая строка длиннее.")
elif len(string1) < len(string2):
    print("Вторая строка длиннее.")
else:
    print("Строки одинаковой длины.")