
"""
Задание 1
Создайте программу, хранящую информацию о вели-
ких баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.
"""
import pprint

def get_basketball_player(basketball_player: list) -> list:
    return basketball_player

def print_result(*args) -> None:
    for element in args:
        print(element)
        #pprint.pprint(element, width=1)
        input('Press to continue...')

def add_basketball_player(surname: str, first_name: str, middle_name: str, growth: str) -> dict:
    global BASKETBALL_PLAYER
    basketball_player = {
        "Surname": surname,
        "First name": first_name,
        "Middle name": middle_name,
        "Growth": growth
    }
    BASKETBALL_PLAYER.append(basketball_player)
    return basketball_player

def del_basketball_player(surname: str) -> dict:
    global BASKETBALL_PLAYER
    deleted_basketball_player = {}
    for index, basketball_player in enumerate(BASKETBALL_PLAYER):
        if basketball_player['Surname'] == surname:
            deleted_basketball_player = basketball_player
            del(BASKETBALL_PLAYER[index])
            return deleted_basketball_player
"""
def update_basketball_player(surname: str) -> dict:
    global BASKETBALL_PLAYER
    for index, basketball_player in enumerate(BASKETBALL_PLAYER):
        if basketball_player['Surname'] == surname:
            first_name = basketball_player["First name"]
            surname = basketball_player["Surname"]
            middle_name = basketball_player["Middle name"]

            new_first_name = input(f"Enter first name ({first_name} - default): ")
            new_surname = input(f"Enter surname ({surname} - default): ")
            new_middle_name = input(f"Enter middle name ({middle_name} - default): ")

            if new_first_name:
                basketball_player['First name'] = new_first_name
            if new_surname:
                basketball_player['Surname'] = new_surname
            if new_middle_name:
                basketball_player['Middle name'] = new_middle_name
            if new_growth['']
            return basketball_player
"""

def search_basketball_player(surname: str) -> dict:
    global BASKETBALL_PLAYER
    for basketball_player in BASKETBALL_PLAYER:
        if basketball_player['Surname'] == surname:
            return basketball_player
    return f"Basketball player {surname} does not exist\n"



if __name__ == "__main__":

    BASKETBALL_PLAYER_LIST = 'list'     # список баскетболистов
    #GROWTH = 'growth'                   # рост
    ADD_BASKETBALL_PLAYER = 'add'       # добавить.
    DEL_BASKETBALL_PLAYER = 'delete'    # удалить.
    UPDATE_BASKETBALL_PLAYER = 'update' # обновить.
    SEARCH_BASKETBALL_PLAYER = 'search' # поиск.
    EXIT = 'q'                          # выход
    BASKETBALL_PLAYER = []

    while True:
        print(f'''
        Choices:
        BASKETBALL_PLAYER_LIST -> {BASKETBALL_PLAYER_LIST}
        ADD_BASKETBALL_PLAYER -> {ADD_BASKETBALL_PLAYER}
        DEL_BASKETBALL_PLAYER -> {DEL_BASKETBALL_PLAYER}
        UPDATE_BASKETBALL_PLAYER -> {UPDATE_BASKETBALL_PLAYER}
        SEARCH_BASKETBALL_PLAYER -> {SEARCH_BASKETBALL_PLAYER}
        EXIT -> {EXIT}
        ---------------------
        ''')
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == BASKETBALL_PLAYER_LIST:
            basketball_player = get_basketball_player(BASKETBALL_PLAYER)
            print_result(basketball_player)

        elif choice == ADD_BASKETBALL_PLAYER:

            surname = input('Enter first surname: ') # фамилие
            first_name = input('Enter first name: ') # имя
            middle_name = input('Enter first middle_name: ') # отчество
            growth = input('Enter first growth: ') #
            basketball_player = add_basketball_player(
                surname=surname,
                first_name=first_name,
                middle_name=middle_name,
                growth = growth
            )
            print_result(basketball_player)

        elif choice == DEL_BASKETBALL_PLAYER:
            surname = input("Enter basketball_player surname: ")
            basketball_player = del_basketball_player(surname=surname)
            print_result(basketball_player)

        elif choice == SEARCH_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            basketball_player = search_basketball_player(surname=surname)
            print_result(basketball_player)

"""
        elif choice == UPDATE_BASKETBALL_PLAYER:
            surname = input("Enter surname: ")
            basketball_player = update_basketball_player(surname=surname)
            print_result(basketball_player)
"""
        
        
            
    