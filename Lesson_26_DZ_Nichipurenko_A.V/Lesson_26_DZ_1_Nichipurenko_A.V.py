'''
Реалізувати паттерн Builder

Приклад взятий з сайту:
https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
'''

class Animal:
    """
    Абстрактное Животное
    """
    legs = 0
    tail = False
    roar = ''

class Mutator:
    """
    Ответственный за размножение
    """
    def mutate(self):
        self.animal = Animal()

class Cat(Mutator):
    """
    Кошка
    """
    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'meowww!'

class Dog(Mutator):
    """
    Собака
    """
    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'woffff!'

class AnimalOwner:
    """
    Владелец питомника
    """
    __mutator = ''
    def set_animal(self, mutator):
        self.__mutator = mutator

    def create_an_animal_for_me(self):
        self.__mutator.mutate()
        self.__mutator.create_legs()
        self.__mutator.create_tail()
        self.__mutator.create_roar()

    def get_animal(self):
        return self.__mutator.animal

c = Cat()
d = Dog()
ao = AnimalOwner()
ao.set_animal(c)
ao.create_an_animal_for_me()
animal = ao.get_animal()
print(animal.roar) 