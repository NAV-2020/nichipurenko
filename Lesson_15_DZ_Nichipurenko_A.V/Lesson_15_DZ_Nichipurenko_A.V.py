

from random import randint, choice


def find_different_elements_set(random_setA, random_setB):
    """
    Створити множини: A, B, C з довільними елементами.
    Знайти:
    1. Різні елементи для A, B
    2. Однакові елементи для A, C
    3. Об'єднання всіх трьох множин.
    """
    return random_setA ^ random_setB


def find_identical_elements_set(random_setA, random_setС):
    
    return random_setA & random_setC


def union_elements_set(random_setA, random_setB, random_setC):
    
    return random_setA | random_setB | random_setB


if __name__ == "__main__":

    alphabet = ['a','b','c','d','e','f', 'g', 'h'] 

    random_setA = set([randint(0, 100) for i in range(10)]) | set([choice(alphabet) for i in range(100)])
    random_setB = set([randint(0, 100) for i in range(10)]) | set([choice(alphabet) for i in range(100)])
    random_setC = set([randint(0, 100) for i in range(10)]) | set([choice(alphabet) for i in range(100)])

    print("Початкова множина A: ", random_setA)
    print("Початкова множина B: ", random_setB)
    print("Початкова множина C: ", random_setC, '\n') 

    print("Різні елементи в множинах A та В: ", find_different_elements_set(random_setA, random_setB), '\n')
    print("Однакові елементи в множинах A та С: ", find_identical_elements_set(random_setA, random_setC), '\n')
    print("Об`єднані елементи A, В та С: ", union_elements_set(random_setA, random_setB, random_setC), '\n')