
from random import randint

def myfunk(random_tuple1, random_tuple2, random_tuple3):
    """
    Есть три кортежа целых чисел необходимо найти
    элементы, которые есть во всех кортежах.
    """
    result = []
    
    for i in random_tuple1:
        if i in random_tuple2 and i in random_tuple3:
            if i not in result:
                result.append(i)
    return tuple(result)

if __name__ == "__main__":

    random_tuple1 = tuple([randint(0, 10) for i in range(10)])
    random_tuple2 = tuple([randint(0, 10) for i in range(10)])
    random_tuple3 = tuple([randint(0, 10) for i in range(10)])

    print("Початковий кортеж 1: ", random_tuple1)
    print("Початковий кортеж 2: ", random_tuple2)
    print("Початковий кортеж 3: ", random_tuple3, '\n') 
    print("Кортеж з елементами які є в заданих кортежах: ", myfunk(random_tuple1, random_tuple2, random_tuple3), '\n')
