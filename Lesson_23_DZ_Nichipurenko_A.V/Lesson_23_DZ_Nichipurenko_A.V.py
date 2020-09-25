"""
Напишіть невеличку програму, яка б на 
Вашу думку демонструвала ПОЛІМОРФІЗМ

Приклад взятий з сайту: https://metanit.com/python/tutorial/7.4.php

З ПОЛІМОРФІЗМом розібрався та зрозумів...!!!
"""

class Person:
    def __init__(self, name, age):
        self._name = name  # устанавливаем имя
        self._age = age  # устанавливаем возраст
 
    @property
    def name(self):
        return self._name
 
    @property
    def age(self):
        return self._age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self._age = age
        else:
            print("Недопустимый возраст")
 
    def display_info(self):
        print(f'"Имя: " {self._name} "\tВозраст: " {self._age}')
 
 
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company
 
    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print(f'"Компания: " {self.company}')
 
 
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university
 
    # переопределение метода display_info
    def display_info(self):
        print(f'"Студент" {self.name} "учится в университете" {self.university}')
 
people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
 
print('-'*40)

for person in people:
    person.display_info()
    print('*'*40)