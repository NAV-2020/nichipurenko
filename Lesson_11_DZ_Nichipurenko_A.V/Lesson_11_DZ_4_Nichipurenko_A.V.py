
"""
Приклад використання lambda функції:
функція, вираховує степінь числа.
"""

print("Функція, вираховує степінь числа.\n")
my_num = int(input("Введіть число: "))
degree = int(input("Введіть значення степені: "))

result = lambda x, y: x ** y
print(result(my_num, degree))
