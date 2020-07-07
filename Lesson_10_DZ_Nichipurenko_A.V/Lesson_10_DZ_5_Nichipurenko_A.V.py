
def my_function_5(my_listOne, my_listTwo):
    """ 
    Задание 5
    Напишите функцию, которая получает два списка в качестве параметра
    и возвращает список, содержащий элементы обоих списков. 
    """

    return my_listOne + my_listTwo


if __name__ == "__main__":

    my_listOne = [int(i) for i in input('Введіть список 1 через пробіл: ').split()]
    my_listTwo = [int(i) for i in input('Введіть список 2 через пробіл: ').split()]
    print("Загальний список: ", my_function_5(my_listOne, my_listTwo), '\n')










