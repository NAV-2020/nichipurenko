'''
Создайте класс Ship, который содержит информацию
о корабле.
С помощью механизма наследования, реализуйте класс 
Frigate (содержит информацию о фрегате), класс Destroyer 
(содержит информацию об эсминце), класс Cruiser 
(содержит информацию о крейсере). Каждый из классов 
должен содержать необходимые для работы методы.
'''

class Ship:
    """General ship information class"""

    valShip = 0

    def __init__(self, сlass_ship: str = 'Undefined', speed: int = 0, displacement: int = 0):
        """Initialize the object"""
        self._сlass_ship = сlass_ship
        self._speed = speed
        self._displacement = displacement
        
        Ship.valShip += 1
    
    #def __del__(self):
        #"""Class destructor"""
        #Ship.valShip -= 1
        #print(f"Left:{Ship.valShip}")

    @property
    def сlass_ship(self) -> str:
        """Returning the property value"""
        return self._сlass_ship

    @сlass_ship.setter
    def сlass_ship(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._сlass_ship = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error entering class value Ship!!!')
            print('The value is initialized by default...')
            input('Press to continue...')
    
    @property
    def speed(self) -> int:
        """Returning the property value"""
        return self._speed

    @speed.setter
    def speed(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._speed = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error entering class value Ship!!!')
            print('The value is initialized by default...')
            input('Press to continue...')
    
    @property
    def displacement(self) -> int:
        """Returning the property value"""
        return self._displacement

    @displacement.setter
    def displacement(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._displacement = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error entering class value Ship!!!')
            print('The value is initialized by default...')
            input('Press to continue...')

    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        Class ship: {self._сlass_ship}
        Speed: {self._speed} (kn)
        Displacement: {self._displacement} (tonne)'''

class Frigate(Ship):
    """Class contains information about the frigate"""

    def __init__(self, name: str = "Undefined", engine_type: str = "Undefined"):
        """Initialize the object"""
        super().__init__(self)
        self._name = name
        self._engine_type = engine_type

    @property
    def name(self) -> str:
        """Returning the property value"""
        return self._name

    @name.setter
    def name(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._name = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')
    
    @property
    def engine_type(self) -> str:
        """Returning the property value"""
        return self._engine_type

    @engine_type.setter
    def engine_type(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._engine_type = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')

    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Name: {self._name}
        Engine type: {self._engine_type}
        '''

class Destroyer(Ship):
    "Class contains information about the destroyer"

    def __init__(self, name: str = "Undefined", count_mines: int = 0):
        super().__init__(self)
        self._name = name
        self._count_mines = count_mines

    @property
    def name(self) -> str:
        """Returning the property value"""
        return self._name

    @name.setter
    def name(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._name = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')
    
    @property
    def count_mines(self) -> int:
        """Returning the property value"""
        return self._count_mines

    @count_mines.setter
    def count_mines(self, val):
        """Setting property value"""
        if isinstance(val, int):
            self._count_mines = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')

    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Name: {self._name}
        Count mines: {self._count_mines}
        '''

class Cruiser(Ship):
    "Class contains information about the cruiser"

    def __init__(self, name: str = "Undefined", cruiser_type: str = "Undefined"):
        super().__init__(self)
        self._name = name 
        self.cruiser_type = cruiser_type

    @property
    def name(self) -> str:
        """Returning the property value"""
        return self._name

    @name.setter
    def name(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._name = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')

    @property
    def cruiser_type(self) -> str:
        """Returning the property value"""
        return self._cruiser_type
    
    @cruiser_type.setter
    def cruiser_type(self, val):
        """Setting property value"""
        if isinstance(val, str):
            self._cruiser_type = val
        else:
            #raise ValueError
            #print('ValueError')
            print('Error while entering value!!!')
            print('The value is initialized by default...')
            input('Press to continue...')
            
    def __str__(self):
        """Method returns a representation of the object"""
        return f'''
        {super().__str__()}
        Name: {self._name}
        Cruiser type: {self._cruiser_type}
        '''
if __name__ == "__main__":
    
    a = Frigate()
    s = Destroyer()
    f = Cruiser()

    a.сlass_ship = "Frigate"
    a.speed = 20
    a.displacement = 6
    a.name = "Vas1" 
    a.engine_type = "Diesel gas turbine"
    print(a)
    print("*"*40)

    s.сlass_ship = "Destroyer"
    s.speed = 20
    s.displacement = 6
    s.name = "Vas2" 
    s.count_mines = 36
    print(s)
    print("*"*40)
    
    f.сlass_ship = "Destroyer"
    f.speed = 20
    f.displacement = 6
    f.name = "Vas3" 
    f.cruiser_type = "Light cruiser"
    print(f)
    print("*"*40)
    
