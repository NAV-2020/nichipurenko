
def my_function_4():
    """ 
    Задание 4
    Напишите функцию, удаляющую из списка целых некоторое заданное число. 
    Из функции нужно вернуть количество удаленных элементов. 
    """
    
    my_lst = [int (i) for i in input('Введіть список через пробіл: ').split()]
    key = int(input("Введіть число: "))

    element = 0
    for i in my_lst:
        if i == key:
            element += 1
            my_lst.remove(i)
    return element

print("Кількість видалених елементів: ", my_function_4(), '\n')