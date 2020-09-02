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

    def __init__(self,
                model: str, 
                year: int, 
                manufacturer:str,
                price: float,
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
        """Destructor call, when the object(car) is removed from the list)"""
        
        print(f"Car {self.model} removed from the list!")
        Car.numberCar -= 1
        if Car.numberCar == 0:
            print("There are no cars in the list!")
        else:
            print(f"Left: {Car.numberCar}.")

    def change_engine_volume(self, engine_vol: float) -> None:
        ''' '''
        try:
            self.engine_volume = float(engine_vol)
        except ValueError as e:
            print(e)
            print("Error: please enter a number of float")

    def set_color(self) -> str:
        self.color = random.choice(Car.colors)
        return self.color

if __name__ == "__main__":
    
    my_car1 = Car('BMW', 1999, 'Germany',3500.2)
    engine_vol = input("Enter engine volume: ")
    my_car1.change_engine_volume(engine_vol)
    my_car1.set_color()

    print(my_car1)
    print('Colors: ', my_car1.color)
    print("Number of cars: ", Car.numberCar)

    #my_car2 = Car('Fiat', 2015, 'Italy', 2000.0)
    #my_car3 = Car('ZAZ', 2000, 'Ukraine', 100.3)
    #del my_car1

    output = input('Press to continue...')


    
   
    