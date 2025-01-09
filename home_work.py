string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if string1.startswith(string2):
    print(f'Первая строка "{string1}" начинается со второй строки "{string2}".')
else:
    print(f'Первая строка "{string1}" не начинается со второй строки "{string2}".')