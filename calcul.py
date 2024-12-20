def calculate(expression):
    # Разделяем строку на элементы (числа и оператор)
    elements = expression.split()

    # Проверяем, что в строке ровно три элемента: два числа и один оператор
    if len(elements) != 3:
        raise ValueError("Строка не соответствует формату: два числа и один оператор")

    # Извлекаем числа и оператор
    a, operator, b = elements

    # Проверяем, что числа являются целыми и находятся в диапазоне от 1 до 10
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Числа должны быть целыми")

    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10")

    # Выполняем операцию в зависимости от оператора
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        result = a // b  # Целочисленное деление
    else:
        raise ValueError("Неподдерживаемая операция")

    return result


# Пример использования
try:
    input_expression = input()
    result = calculate(input_expression)
    print("Результат:", result)
except Exception as e:
    print("Ошибка:", e)