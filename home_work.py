def multiply_all(*args):

    result = 1
    for number in args:
        result *= number
    return result

result = multiply_all(1, 2, 3, 4, 5)
print("Произведение:", result)