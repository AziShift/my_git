def is_substring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if is_substring(string1, string2):
    print(f'"{string2}" является подстрокой "{string1}".')
else:
    print(f'"{string2}" не является подстрокой "{string1}".')