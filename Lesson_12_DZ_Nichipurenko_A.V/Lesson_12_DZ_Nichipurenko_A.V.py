
"""
Написати функцію-декоратор, яка підносить до квадрату значення, 
що повертає функція, до якої декоратор застосовується.
"""

def decorFunc(func):
    
    def funcOne(arg1, arg2, arg3):
        varOne = func(arg1, arg2, arg3)
        result = [i**2 for i in varOne]
        return result 
    return funcOne 


@decorFunc
def my_func(val1,val2, val3):
    var_result = [i for i in range (val1, val2, val3)]
    print("Початковий список значень: ", var_result, '\n')
    return var_result

print("*"*50)
print("Задайте діапазон чисел для піднесення до квадрату.\n")
var1 = int(input("Введіть початкове значення :"))
var2 = int(input("Введіть кінцеве значення :"))
var3 = int(input("Введіть крок між значеннями :"))

print("Значення піднесені до квадрату: ", my_func(var1, var2, var3))
