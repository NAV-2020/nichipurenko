'''
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).
'''
import pickle

def print_result(country_capital) -> None:
    '''Data output function(print)'''
    print('Data list: ')
    for key, value in country_capital.items():
        print(key,'-', value)
    input('Press to continue...')

def add_countryCapital() -> dict:
    '''The function adds data to the dictionary'''
    countryCapital = {}
    country = input('Enter your country: ')
    capital = input('Enter the capital: ')
    countryCapital[country] = capital
    print(dict(countryCapital.items()))
    return countryCapital

def del_country(country_capital: dict, country: str):
    '''Country data deletion function'''
    if country in country_capital.keys():
        country_capital.pop(country)
    else:
        print(f'Country {country} does not exist!')

def search_countri(country: str) -> None:
    '''Country data search function'''
    if country in country_capital.keys():
        print(country, '-', country_capital.get(country))
    else:
        print(f'Country {country} does not exist!')

def up_country(country_capital: dict, country: str) -> None:
    '''Capital change function'''
    if country in country_capital.keys():
        capital = input('Enter the new capital: ')
        country_capital[country] = capital
    else:
        print(f'Country {country} does not exist!')


def saverData(myData: str, country_capital: dict) -> None: # сохранить в файле с упаковкой
    '''Saving data to a file with packaging'''
    with open(myData, mode='wb') as f:
        pickle.dump(country_capital, f)
        print('File saved.')
        
def loaderData(myData: str) -> dict: # загрузить файл с распаковкой
    '''Loading data from unpacking'''
    with open(myData, mode='rb') as f:
        res = pickle.load(f)
        print('File downloaded.')
        return res
       

if __name__ == "__main__":
    
    myData = 'F:\\IT_School\\nichipurenko\\Lesson_19_DZ_Nichipurenko_A.V\\data.bin'

    #! CONSTS
    COUNTRY_CAPITAL_LIST = 'list'
    ADD_COUNTRY_CAPITAL = 'add'
    DEL_COUNTRY_CAPITAL = 'delete'
    SEARCH_COUNTRY_CAPITAL = 'search'
    UPDATE_COUNTRY_CAPITAL = 'update'
    SAVE = 'save' # сохранить изменения в файле
    LOAD = 'load' # загрузить файл 
    EXIT = 'q'

    country_capital = {}
 
    while  True:
        print(f'''
        Choices:
        List of countries -> {COUNTRY_CAPITAL_LIST}
        Add -> {ADD_COUNTRY_CAPITAL}
        Delete -> {DEL_COUNTRY_CAPITAL}
        Search -> {SEARCH_COUNTRY_CAPITAL}
        Update -> {UPDATE_COUNTRY_CAPITAL}
        Save ->  {SAVE}
        Load -> {LOAD}
        EXIT -> {EXIT}
        ---------------------
        ''')
    
        choice = input('Make your choice: ')

        if choice == EXIT:
            break

        elif choice == COUNTRY_CAPITAL_LIST:
            print_result(country_capital)

        elif choice == ADD_COUNTRY_CAPITAL:
            result = add_countryCapital()
            country_capital.update(result) 
            input('Press to continue...')       
        
        elif choice == DEL_COUNTRY_CAPITAL:
            country = input('Enter your country: ')
            print(country, '-', country_capital.get(country))
            del_country(country_capital, country=country)
            input('Press to continue...')
        
        elif choice == SEARCH_COUNTRY_CAPITAL:
            country = input('Enter your country: ')
            search_countri(country=country)
            input('Press to continue...')

        elif choice == UPDATE_COUNTRY_CAPITAL:
            country = input('Enter your country: ')
            up_country(country_capital, country)
            input('Press to continue...')

        elif choice == SAVE:
            saverData(myData, country_capital)
            input('Press to continue...')

        elif choice == LOAD:
            resData = loaderData(myData)
            if resData != None:
                country_capital.update(resData)
            else:
                print('No data in file!!!')
            input('Press to continue...')