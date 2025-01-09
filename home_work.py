def calculate(operation, *args):
    if operation == "add":
        return sum(args) 
    elif operation == "multiply":
        result = 1
        for number in args:
            result *= number 
        return result
    else:
        raise ValueError("Неверная операция. Используйте 'add' или 'multiply'.")


sum_result = calculate("add", 1, 2, 3, 4, 5)
print("Сумма:", sum_result)

multiply_result = calculate("multiply", 1, 2, 3, 4, 5)
print("Произведение:", multiply_result)