print('''
Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
1. Сформировать третий список, содержащий элементы
обоих списков;
2. Сформировать третий список, содержащий элементы
обоих списков без повторений;
3. Сформировать третий список, содержащий элементы
общие для двух списков;
4. Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
5. Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков.
''')

my_listOne = [int(i) for i in input('Введіть список 1 через пробіл: ').split()]
my_listTwo = [int(i) for i in input('Введіть список 2 через пробіл: ').split()]

print()

my_act = int(input("""Виберіть дію для продовження:

1 - Список який містить елементи двух списків
2 - Список який містить елементи списків без повторень	
3 - Список який містить спільні елементи списків	
4 - Список який містить унікальні елементи списків
5 - Список який містить мінімальні та максимальні значення двух списків

"""))

#my_listOne = [16, 11, 12, 2, 4, 9, 13, 1]   # тест
#my_listTwo = [8, 4, 6, 2, 10, 3]            # тест


my_list2 = [] # змінна з результатом завдання 2
my_list3 = [] # змінна з результатом завдання 3
my_list4 = [] # змінна з результатом завдання 4
my_list5 = [] # змінна з результатом завдання 5


##################-1-####################

if my_act == 1:
    my_list1 = my_listOne + my_listTwo # змінна my_list1 з результатом завдання 1
    print("Елементи двух списків: ", my_list1, '\n')

##################-2-####################

elif my_act == 2:
    my_listTemp = my_listOne[:]
    for i in my_listTwo:
        if i not in my_listTemp:
            my_listTemp.append(i)
    for i in my_listTemp:
        if i not in my_list2:
            my_list2.append(i)
    print("Елементи двух списків без повторень: ", my_list2, '\n')

##################-3-####################

elif my_act == 3:
    for i in my_listTwo:
	    if i in my_listOne and i not in my_list3:
		    my_list3.append(i)	
    print("Список який містить спільні елементи списків: ", my_list3, '\n')

##################-4-####################

elif my_act == 4:
    for i in my_listOne:
	    if i not in my_listTwo and i not in my_list4:
		    my_list4.append(i)
    for i in my_listTwo:
	    if i not in my_listOne and i not in my_list4:
		    my_list4.append(i)
    print("Список який містить унікальні елементи списків: ", my_list4, '\n')

##################-5-####################

elif my_act == 5:
    my_list5.append(min(my_listOne))
    my_list5.append(max(my_listOne))
    my_list5.append(min(my_listTwo))
    my_list5.append(max(my_listTwo))
    print("Список який містить мінімальні та максимальні значення двух списків: ", my_list5, '\n')