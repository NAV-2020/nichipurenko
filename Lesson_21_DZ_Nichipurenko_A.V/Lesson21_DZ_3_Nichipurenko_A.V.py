'''
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
'''

class Stadium:
    """Class represents a list of stadiums"""
    numberStadium = 0

    def __init__(self,
                stadium_name: str,
                opening_date: str,
                country: str,
                city: str,
                capacity: int):
        """Initializes the book data attributes"""
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

        Stadium.numberStadium += 1

    def __str__(self):
        '''Returns data'''
        return f'''
        Stadium name: {self.stadium_name} 
        Opening date: {self.opening_date} 
        Country: {self.country} 
        City: {self.city} 
        Capacity: {self.capacity}
        '''

    def __del__(self):
        """Destructor call, when the object(Stadium) is removed from the list"""
        print(f'Stadium {self.stadium_name} removed from the list!')
        Stadium.numberStadium -= 1
        if Stadium.numberStadium == 0:
            print("No stadiums listed!")
        else:
            print(f"Left: {Stadium.numberStadium}.")



if __name__ == "__main__":
    
    my_stadium1 = Stadium('"Olympic"', '12.11.2000', 'England', 'London', 5500)
    print(my_stadium1)
    my_stadium2 = Stadium('"Spartacus"', '02.01.1980', 'France', 'Paris', 4300)
    print(my_stadium2)

    print('Number of stadiums: ', Stadium.numberStadium)
    #del my_stadium1
    #print('Number of stadiums: ', Stadium.numberStadium)

    output = input('Press to continue...')