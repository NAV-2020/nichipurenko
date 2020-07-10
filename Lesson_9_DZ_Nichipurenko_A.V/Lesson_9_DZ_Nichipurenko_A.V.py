''' Завдання 1 '''

def text():
    print('''Задание 1
Напишите функцию, которая отображает на экран форматированный текст, 
указанный ниже:
    “Don't compare yourself with anyone in this world...
    if you do so, you are insulting yourself.”
                                    Bill Gates \n''')
    print("#"*80, '\n')
    word1 = "  " + '''"Don't compare yourself with anyone in this world...'''
    word2 = "  " + ''' if you do so, you are insulting yourself." '''
    word3 = "\t"*4 + '''   Bill Gates''' 
    print(word1, word2, word3, sep="\n", end="")

''' Завдання 2 '''

def band(numX, numY):
    if numX < numY:
        result = [i for i in range(numX, numY) if i % 2==0]
        print('''Всі парні числа в указаному діапазоні: ''', result)
    #elif numX > numY:
        #result = [i for i in range(numY, numX) if i % 2==0]
        #print('''Всі парні числа в указаному діапазоні: ''', result)

''' Завдання 3 '''

def square(my_Width, my_Height):
    
    outlineSq = input("\nВведіть символ для контуру: ")
    empty_fil_Sq = input('''\nВведыть
    True - для заповнення квалрата
    False - для пустого квадрат\n''')
    if empty_fil_Sq == "True":
        tmp = outlineSq
    elif empty_fil_Sq == "False":
        tmp = " "
    for i in range(my_Height):
	    if i == 0 or i == my_Height - 1:
		    print(outlineSq * my_Width)
	    else:
		    print(outlineSq+tmp * (my_Width - 2) + outlineSq)

''' Завдання 4 '''

def minNumber(me_Num):
    if 5 == len(my_Num):
        return (min(my_Num))

''' Завдання 5 '''

def multiplicNum(my_X, my_Y):
    if my_X < my_Y:
	    result = 1
	    for i in range(my_X, my_Y+1):
		    result *= i
	    return (result)
    elif my_X > my_Y:
	    result = 1
	    for i in range(my_Y, my_X+1):
		    result *= i
	    return (result)

''' Завдання 6 '''

def countsNum(my_Num):
    return(len(my_Num))

''' Завдання 7 '''

def polyDrome(my_Num):
    if my_Num == my_Num[::-1]:
        return True
    else:
        return False

#####################################################################################

print('''
Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
    “Don't compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                        Bill Gates

Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними.

Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.

Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров.

Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами.

Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4.

Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром.''', '\n')

my_Value = int(input('''Виберіть завдання:
1  <- Завдання 1
2  <- Завдання 2
3  <- Завдання 3
4  <- Завдання 4
5  <- Завдання 5
6  <- Завдання 6
7  <- Завдання 7\n
'''))

if my_Value == 1: # Відображення на екрані форматованого тексту
	text()


elif my_Value == 2:
    print('''Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними.\n''')
    numX = int(input("Введіть початок діапазону:\n"))
    numY = int(input("Введіть кінець діапазону:\n"))
    band (numX, numY)


elif my_Value == 3:
    print('''Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.\n''')
    my_Width = int(input("Введіть ширину квадрата: ")) 
    my_Height = int(input("Введіть висоту квадрата: "))
    square(my_Width, my_Height)


elif my_Value == 4:
    print('''Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров.\n''')
    my_Num = [int(i) for i in input("Введіть 5 чисел через пробіл: ").split()]
    if minNumber(my_Num) != None:
        print ("Мінімальне число:", minNumber(my_Num),'\n')
    else:
        print("Введено НЕ 5 чисел!!!\n ")
        

elif my_Value == 5:
    print ('''Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 
25 — нижняя граница), их нужно поменять местами.\n''')
    my_X = int(input("Введите начало диапазона\n"))
    my_Y = int(input("Введите конец диапазона\n"))
    print ('''Результат множення чисел вказаного діапазона:''', multiplicNum(my_X, my_Y)) 


elif my_Value == 6:
    print('''Задание 6
Напишите функцию, которая считает количество цифр в числе. Число 
передаётся в качестве параметра. Из функции нужно вернуть полученное 
количество цифр. Например, если передали 3456, количество цифр будет 4.\n''')
    my_Num = input("Введіть число: ")
    print("Кількість чисел в заданому числі: ", countsNum(my_Num),'\n')


elif my_Value == 7:
    print('''Задание 7
Напишите функцию, которая проверяет является ли число палиндромом. 
Число передаётся в качестве параметра. Если число палиндром нужно 
вернуть из функции true, иначе false. «Палиндром» — это число, 
у которого первая часть цифр равна второй перевернутой части цифр. 
Например, 123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром, 
а 421987 — не палиндром.\n''')
    my_Num = input("Введіть число: ")
    if polyDrome(my_Num) == True:
        print("Число полідром: ", my_Num,'\n')
    elif polyDrome(my_Num) == False:
        print("Число НЕ полідром: ", my_Num,'\n')


else:
    print('''Ввід не коректний.
Почніть спочатку!!!\n''')