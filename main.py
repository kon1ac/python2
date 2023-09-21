import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Деление на ноль недопустимо")


def exponent(a, b):
    return a ** b


def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError("Недопустимое значение для квадратного корня")


def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        raise ValueError("Недопустимое значение для факториала")


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Неверный формат числа. Пожалуйста, повторите ввод.")


def get_operation_input(prompt):
    valid_operations = ["+", "-", "*", "/", "^", "sqrt", "!", "sin", "cos", "tan"]
    while True:
        operation = input(prompt)
        if operation in valid_operations:
            return operation
        else:
            print("Неподдерживаемая операция. Пожалуйста, повторите ввод.")


def perform_operation(operation, a, b=None):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    elif operation == "^":
        return exponent(a, b)
    elif operation == "sqrt":
        return square_root(a)
    elif operation == "!":
        return factorial(a)
    elif operation == "sin":
        return sin(a)
    elif operation == "cos":
        return cos(a)
    elif operation == "tan":
        return tan(a)


def main():
    operation = get_operation_input("Введите операцию (+, -, *, /, ^, sqrt, !, sin, cos, tan): ")

    if operation in ["+", "-", "*", "/", "^"]:
        num1 = get_number_input("Введите первое число: ")
        num2 = get_number_input("Введите второе число: ")
        result = perform_operation(operation, num1, num2)
        print("Результат:", result)
    elif operation in ["sqrt", "!"]:
        num = get_number_input("Введите число: ")
        result = perform_operation(operation, num)
        print("Результат:", result)
    elif operation in ["sin", "cos", "tan"]:
        num = get_number_input("Введите угол в радианах: ")
        result = perform_operation(operation, num)
        print("Результат:", result)


if __name__ == "__main__":
    main()
