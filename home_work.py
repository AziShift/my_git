string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if string1.lower() == string2.lower():
    print("Строки одинаковые (без учета регистра).")
else:
    print("Строки разные.")