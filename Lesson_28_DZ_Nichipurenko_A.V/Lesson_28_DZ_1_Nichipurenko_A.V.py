"""
Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо 
сохранить в список (тип списка нужно выбрать в зависимости от поставленной
ниже задачи). После чего нужно показать меню, в котором предложить 
пользователю набор пунктов:
1. Добавить новое число в список (если такое число существует в списке, 
нужно вывести сообщение пользователю об этом, без добавления числа).
2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры 
число для удаления).
3. Показать содержимое списка (в зависимости от выбора пользователя список 
нужно показать с начала или с конца).
4. Проверить есть ли значение в списке.
5. Заменить значение в списке (пользователь определяет заменить ли только 
первое вхождение или все вхождения).
    В зависимости от выбора пользователя выполняется действие, после чего меню 
отображается снова.
"""

def add_lst(val_lst: int)->None:
    """The function forms the initial list."""
    lst.append(val_lst)

def verify_val(val_add: int)->bool:
    """Function for checking if a number is in the list."""
    if val_add not in lst:
        return True
    else:
        return False

def add_num(val_add: int)->bool:
    """The function adds a number to the list."""
    if verify_val(val_add):
        lst.append(val_add)
        return True
    else:
        return False

def del_num(val_del: int)-> bool:
    """The function removes a number from the list."""
    for id, element in enumerate(lst):
        if element == val_del:
            del lst[id]
            return True

def show_lst(val_show: int)->list:
    """List output function."""
    if val_show == 1:
        return lst
    elif val_show == 2:
        return lst[::-1]
    else:
        print("The choice was made incorrectly!!!")

def replace_val(rep_val: int, new_val: int, flag_val: int)->bool:
    """Number replacement function."""
    if flag_val == 1:
        if rep_val in lst:
            for id, element in enumerate(lst):
                if element == rep_val:
                    lst[id] = new_val
                    return True
    elif flag_val == 2:
        if rep_val in lst:
            for id, element in enumerate(lst):
                if element == rep_val:
                    lst[id] = new_val
            return True
    

if __name__ == "__main__":

    lst = []
    
    while True:
        
        print('*'*60)
        print("List entry:")
        print("""    
        1. Add a list item ---------------------> add 
        2. Proceed -----------------------------> p
            """)
        print('*'*60)

        choice = input("Сhoice: ") 

        if choice == 'add':
            add_lst(val_lst = int(input("Enter one number: ")))
            print(show_lst(val_show=1))

        elif choice == 'p':
            break
        
    
    while True:

        print('*'*60)
        print("Make your choice:")
        print("""    
        1. Add new number ----------------------> add
        2. Remove all occurrences of a number --> del
        3. Show list contents ------------------> show
        4. Check if a value is in the list -----> verify
        5. Replace value in list ---------------> replace 
        6. Exit --------------------------------> q
            """)
        print('*'*60)

        pick = input("Сhoice: ")

        if pick == 'q':
            break
            
        elif pick == 'add':
            result_add = add_num(int(input("Insert the number: ")))
            if result_add:
                print("Number added to list.")
                print(show_lst(val_show=1))
                input("Press to continue...")
            else:
                print("Number already exists in the list!!!")
                input("Press to continue...")
        
        elif pick == 'del':
            result_del = del_num(int(input("Insert the number: ")))
            if result_del:
                print("Number removed from the list.")
                print(show_lst(val_show=1))
                input("Press to continue...")
            else:
                print("There is no number to remove from the list!!!")
                input("Press to continue...")

        elif pick == 'show':
            print("""
        How to display a list?
        1. Show from the beginning of the list --> 1
        2. Show from the end of the list --------> 2
                    """)
            print("Result: ", show_lst(int(input("Enter: "))))
            input('Press to continue...')
            
        elif pick == 'verify':
            val_ver = int(input("Enter a number to check: "))
            if verify_val(val_ver):
                print(f"{val_ver} NOT on the list!")
                input("Press to continue...")
            else:
                print(f"{val_ver} is on the list.")
                input("Press to continue...")

        elif pick == 'replace':
            print("List: ", show_lst(val_show=1))
            rep_val = int(input("List value: ")) 
            new_val = int(input("New value: ")) 
            flag_val = int(input("""
                1. Replace the first occurrence in the list -> 1
                2. Replace all occurrences in the list ------> 2
                Enter: """)) 
            if replace_val(rep_val, new_val, flag_val):
                print("Replacement was successful.")
                print("List: ", show_lst(val_show=1))
                input("Press to continue...")

            


