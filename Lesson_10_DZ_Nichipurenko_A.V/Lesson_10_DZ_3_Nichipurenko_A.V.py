
def my_function_3(number):
    """ 
    Задание 3
    Напишите функцию, определяющую количество простых чисел в списке целых. 
    Список передаётся в качестве параметра. Полученный результат возвращается из функции. 
    """

    prime_numbers = []
    for num in range(2, number + 1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
                break
        if prime:
            prime_numbers.append(num)
            #print("Список простіх чисел:", num)
    print()
    print("Список простих чисел: ", prime_numbers, '\n')
    return len(prime_numbers)


if __name__ == "__main__":
    
    my_result = my_function_3(number = int(input("Введіть кінець списку: ")))
    print("Кількість простих чисел: ", my_result, '\n')
