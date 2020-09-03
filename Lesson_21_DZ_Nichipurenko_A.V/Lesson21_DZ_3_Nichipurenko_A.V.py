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
                capacity: int = 0,
                country: str = '',
                city: str = '',
                ):
        """Initializes the book data attributes"""
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.capacity = capacity
        self.country = country
        self.city = city


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

    @property
    def set_country(self):
        return self.country
		
    @set_country.setter
    def set_country(self, value):
        self.country = value.title()
	
    @property
    def set_city(self):
        return self.city
		
    @set_city.setter
    def set_city(self, value):
        self.city = value.title()
    



if __name__ == "__main__":
    
    my_stadium1 = Stadium('"Olympic"', '12.11.2000', 5500) 
    my_stadium1.set_country = "England"   
    my_stadium1.set_city = "London"     

    print(my_stadium1)

    my_stadium2 = Stadium('"Spartacus"', '02.01.1980', 4300)
    my_stadium2.set_country = "France" 
    my_stadium2.set_city = "Paris"

    print(my_stadium2)

    print('Number of stadiums: ', Stadium.numberStadium)
    #del my_stadium1
    #print('Number of stadiums: ', Stadium.numberStadium)

    output = input('Press to continue...')

    #('"Olympic"', '12.11.2000', 'England', 'London', 5500)
    #('"Spartacus"', '02.01.1980', 'France', 'Paris', 4300)