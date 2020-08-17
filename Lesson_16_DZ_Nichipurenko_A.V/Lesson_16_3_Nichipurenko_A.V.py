"""
Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
название должности, номер кабинета, skype. Требуется
реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
информации.
"""

import pprint

def get_company_employee(company_employee: list) -> list:
    return company_employee

def print_result(*args) -> None:
    for element in args:
        print(element)
        #pprint.pprint(element, width=1)
        input('Press to continue...')

def add_company_employee(surname_name_middle_name: str, telephone: str, emai_l: str, 
                            post: str, room_number: str, skype: str) -> dict:
    global COMPANY_EMPLOYEE
    company_employee = {
        "Surname, name, middle name": surname_name_middle_name,
        "Telephone": telephone,
        "Email": emai_l,
        "Post": post,
        "Room number": room_number,
        "Skype": skype

    }
    COMPANY_EMPLOYEE.append(company_employee)
    return company_employee

def del_company_employee(surname_name_middle_name: str) -> dict:
    global COMPANY_EMPLOYEE
    deleted_company_employee = {}
    for index, company_employee in enumerate(COMPANY_EMPLOYEE):
        if company_employee['Surname, name, middle name'] == surname_name_middle_name:
            deleted_company_employee = company_employee
            del(COMPANY_EMPLOYEE[index])
            return deleted_company_employee

def search_company_employee(surname_name_middle_name: str) -> dict:
    global COMPANY_EMPLOYEE
    for company_employee in COMPANY_EMPLOYEE:
        if company_employee['Surname, name, middle name'] == surname_name_middle_name:
            return company_employee
    return f"The employee in the list {surname_name_middle_name} does not exist\n"

def update_company_employee(surname_name_middle_name: str) -> dict:
    pass
    """
    global COMPANY_EMPLOYEE
    for index, company_employee in enumerate(COMPANY_EMPLOYEE):
        if company_employee['Surname, name, middle name'] != surname_name_middle_name:
            print('There is no employee with such data !!!')
            input('Press to continue...')

        elif company_employee['Surname, name, middle name'] == surname_name_middle_name:

            surname_name_middle_name = company_employee["Surname, name, middle name"]
            telephone = company_employee["Telephone"]
            emai_l = company_employee["Email"]
            post = company_employee["Post"]
            room_number = copany_employee["Room number"]
            room_skype = copany_employee["Skype"]
            
            new_surname_name_middle_name = input(f"Enter surname, name, middle name ({surname, name, middle name} - default): ") # фамилие, имя, отчество
            new_telephone = input(f"Enter telephone ({telephone} - default): ") # телефон
            new_emai_l = input(f"Enter email ({emai_l} - default): ") # email
            new_post = input(f"Enter post({post} - default): ") # должность
            new_room_number = input(f"Enter room number({room_number} - default): ") # номер кабинета
            new_skype = input(f"Enter skype({skype} - default): ") # skype

            if new_surname_name_middle_name:
                company_employee['Surname, name, middle name'] = new_surname_name_middle_name
            if new_telephone:
                company_employee['Telephone'] = new_telephone
            if new_emai_l:
                company_employee['Email'] = new_emai_l
            if new_post:
                company_employee['Post'] = new_post
            if new_room_number:
                company_employee['Room number'] = new_room_number
            if new_skype:
                company_employee['Skyper'] = new_skype
            return company_employee
"""


if __name__ == "__main__":

    COMPANY_EMPLOYEE_LIST = 'list'     # список баскетболистов
    ADD_COMPANY_EMPLOYEE = 'add'       # добавить
    DEL_COMPANY_EMPLOYEE = 'delete'    # удалить
    UPDATE_COMPANY_EMPLOYEE = 'update' # обновить
    SEARCH_COMPANY_EMPLOYEE = 'search' # поиск
    EXIT = 'q'                          # выход
    COMPANY_EMPLOYEE = []

    while True:
        print(f'''
        Choices:
        COMPANY_EMPLOYEE_LIST -> {COMPANY_EMPLOYEE}
        ADD_COMPANY_EMPLOYEE -> {ADD_COMPANY_EMPLOYEE}
        DEL_COMPANY_EMPLOYEE -> {DEL_COMPANY_EMPLOYEE}
        UPDATE_COMPANY_EMPLOYEE -> {UPDATE_COMPANY_EMPLOYEE}
        SEARCH_COMPANY_EMPLOYEE -> {SEARCH_COMPANY_EMPLOYEE}
        EXIT -> {EXIT}
        ---------------------
        ''')
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == COMPANY_EMPLOYEE_LIST:
            company_employee = get_company_employee(COMPANY_EMPLOYEE)
            print_result(company_employee)

        elif choice == ADD_COMPANY_EMPLOYEE:
            surname_name_middle_name = input('Enter surname, name, middle name: ') # фамилие, имя, отчество
            telephone = input('Enter telephone: ') # телефон
            emai_l = input('Enter email: ') # email
            post = input('Enter post: ') # должность
            room_number = input('Enter room number: ') # номер кабинета
            skype = input('Enter skype: ') # skype
            company_employee = add_company_employee(
                surname_name_middle_name = surname_name_middle_name,
                telephone = telephone,
                emai_l = emai_l,
                post = post,
                room_number = room_number,
                skype = skype
            )
            print_result(company_employee)

        elif choice == DEL_COMPANY_EMPLOYEE:
            surname = input("Enter surname, name, middle name: ")
            company_employee = del_company_employee(surname_name_middle_name = surname_name_middle_name)
            print_result(company_employee)

        elif choice == SEARCH_COMPANY_EMPLOYEE:
            surname_name_middle_name = input('Enter surname, name, middle name: ')
            company_employee = search_company_employee(surname_name_middle_name = surname_name_middle_name)
            print_result(company_employee)

        elif choice == UPDATE_COMPANY_EMPLOYEE:
            surname_name_middle_name = input('Enter surname, name, middle name: ')
            company_employee = update_company_employee(surname_name_middle_name = surname_name_middle_name)
            if company_employee != None:  
                print_result(company_employee)