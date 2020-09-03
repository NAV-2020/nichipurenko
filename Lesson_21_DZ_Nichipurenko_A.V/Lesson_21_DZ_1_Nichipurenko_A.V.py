"""
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, 
производителя, объем двигателя, цвет машины, цену.
Реализуйте методы класса для ввода данных, вывода 
данных, реализуйте доступ к отдельным полям через 
методы класса. 
"""
import random

class  Car:
    """This class represents a list of vehicles with parameters."""

    numberCar = 0
    colors = ['RED', 'GREEN', 'GRAY', 'BLACK']
    price = [1000.0, 1500.30, 2200.40, 3200.0]

    def __init__(self,
                model: str, 
                year: int, 
                manufacturer:str,
                price: float = 0.0,
                color: str = '',
                engine_volume: float = 0.0):
        """Initializes the vehicle data attributes"""

        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.price = price
        self.color = color
        self.engine_volume = engine_volume

        Car.numberCar += 1

    def __str__(self):
        '''Returns data'''
        return f'''
        Model: {self.model} 
        Year of issue: {self.year} 
        Manufacturer: {self.manufacturer} 
        Engine volume: {self.engine_volume} 
        Color: {self.color} 
        Price: {self.price}
        '''

    def __del__(self):
        """Destructor call, when the object(Car) is removed from the list."""
        print(f"Car {self.model} removed from the list!")
        Car.numberCar -= 1
        if Car.numberCar == 0:
            print("There are no cars in the list!")
        else:
            print(f"Left: {Car.numberCar}.")

    def change_engine_volume(self, engine_vol: float) -> None:
        '''Method for entering engine displacement.'''
        try:
            self.engine_volume = float(engine_vol)
        except ValueError as e:
            #print(e)
            print("Error: please enter a number of float")

    def set_color(self) -> str:
        '''Random car color selection method.'''
        self.color = random.choice(Car.colors)
        return self.color

    @property
    def set_price(self) -> float:
        '''Returns the price of a car'''
        return Car.price[self.price]
		
    @set_price.setter
    def set_price(self, val: int) -> None:
	    self.price = Car.price[val]

if __name__ == "__main__":
    
    my_car1 = Car('BMW', 1999, 'Germany')
    engine_vol = input("Enter engine volume car 1: ")
    my_car1.change_engine_volume(engine_vol)
    my_car1.set_price = 1
    my_car1.set_color()
    print(my_car1)

    my_car2 = Car('Fiat', 2015, 'Italy')
    engine_vol = input("Enter engine volume car 2: ")
    my_car2.change_engine_volume(engine_vol)
    my_car2.set_price = 2
    my_car2.set_color()
    print(my_car2)

    print("Number of cars: ", Car.numberCar)
    output = input('Press to continue...')
    
    #del my_car1
    

    
   
    