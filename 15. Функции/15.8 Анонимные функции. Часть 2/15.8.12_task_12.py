from functools import reduce

def evaluate(coefficients, x):
    # Используем reduce для вычисления значения многочлена
    return reduce(lambda acc, coeff: acc * x + coeff, coefficients)

# Чтение входных данных
coefficients = list(map(int, input().split()))  # Чтение коэффициентов многочлена
x = int(input())  # Чтение значения переменной x

# Вызов функции evaluate и вывод результата
print(evaluate(coefficients, x))