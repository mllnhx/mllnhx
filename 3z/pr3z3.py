# Запрос ввода двух чисел
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

# Проверка условия и изменение числа a при необходимости
if abs(a) > abs(b):
    a = a / 5

# Вывод значений переменных
print(f"Измененное число a: {a}")
print(f"Число b: {b}")
