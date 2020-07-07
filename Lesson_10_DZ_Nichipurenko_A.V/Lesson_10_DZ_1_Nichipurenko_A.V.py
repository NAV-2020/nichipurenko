
def my_function_1(my_lst):
    """ 
    Задание 1
    Напишите функцию, вычисляющую произведение элементов списка целых. 
    Список передаётся в качестве параметра. Полученный результат возвращается из функции.
    """

    result = 1
    print("Список елементів: ", my_lst, '\n')
    for i in my_lst:
        result *= i
    return result

if __name__ == "__main__":
    
    my_result = my_function_1(my_lst = [int (i) for i in input('Введіть список через пробіл: ').split()])
    print("Результат множення чисел: ", my_result, '\n')
