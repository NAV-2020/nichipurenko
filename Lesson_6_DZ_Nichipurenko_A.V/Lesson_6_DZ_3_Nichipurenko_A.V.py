"""
Задание 3
Пользователь вводит с клавиатуры два числа (начало
и конец диапазона). Требуется проанализировать все числа
в этом диапазоне. Вывод на экран должен проходить по
правилам, указанным ниже.
    Если число кратно 3 (делится на 3 без остатка) нужно
вывести слово Fizz. Если число кратно 5 нужно вывести
слово Buzz. Если число кратно 3 и 5 нужно вывести
Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
само число.

"""

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

sum_A = 0

if num_1 < num_2:   # якщо введено спочатку менше число

    num_2 += 1 #для вирівнювання числового ряду

    for i in range(num_1 , num_2):       # Всі числа діапазона
        if i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")
    
        elif i % 3 and i % 5 == 0:
            print("Fzz Buzz")

        elif i % 3 and i % 5 !=0:
            print(i)

else:           # якщо введено спочатку більше число
   
    num_1 += 1 #для вирівнювання числового ряду

    for i in range(num_2, num_1):       # Всі числа діапазона
        if i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")
    
        elif i % 3 and i % 5 == 0:
            print("Fzz Buzz")

        elif i % 3 and i % 5 !=0:
            print(i)