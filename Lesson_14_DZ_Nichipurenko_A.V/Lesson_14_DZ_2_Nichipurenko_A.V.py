from random import randint

def myfunk(random_tuple1, random_tuple2, random_tuple3):
    """
    Есть три кортежа целых чисел необходимо найти
    элементы, которые уникальны для каждого списка.
    """
    result = []

    for i in random_tuple1:
        if i not in random_tuple2 and i not in random_tuple3:
            if i not in result:
                result.append(i)
    
    for q in random_tuple2:
        if q not in random_tuple1 and q not in random_tuple3:
            if q not in result:
                result.append(q)
    
    for w in random_tuple3:
        if w not in random_tuple2 and w not in random_tuple1:
            if w not in result:
                result.append(w)
    return tuple(result)

if __name__ == "__main__":

    random_tuple1 = tuple([randint(0, 10) for i in range(10)])
    random_tuple2 = tuple([randint(0, 10) for i in range(10)])
    random_tuple3 = tuple([randint(0, 10) for i in range(10)])

    print("Початковий кортеж 1: ", random_tuple1)
    print("Початковий кортеж 2: ", random_tuple2)
    print("Початковий кортеж 3: ", random_tuple3, '\n') 
    print("Кортеж з елементами які унікальні в заданих кортежах: ", myfunk(random_tuple1, random_tuple2, random_tuple3), '\n')