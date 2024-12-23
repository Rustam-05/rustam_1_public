def main(input_str: str):
    """
    Основная функция, принимает строку с арифметическим выражением и возвращает результат.
    """
    operation = input_str.split()

    if (len(operation) != 3 or operation[1] not in ['+', '-', '*', '/'] or
            not operation[0].isdigit() or not operation[2].isdigit()):
        raise ValueError("Формат операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

    numder_1, operator, numder_2 = operation

    numder_1 = int(numder_1)
    numder_2 = int(numder_2)

    if not (1 <= numder_1 <= 10 and 1 <= numder_2 <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10")

    if operator == '+':
        result = numder_1 + numder_2
    elif operator == '-':
        result = numder_1 - numder_2
    elif operator == '*':
        result = numder_1 * numder_2
    elif operator == '/':
        if numder_2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = numder_1 // numder_2

    return str(result)

