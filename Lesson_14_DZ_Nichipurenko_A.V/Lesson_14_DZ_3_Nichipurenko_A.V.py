from random import randint

def myfunk(random_tuple1, random_tuple2, random_tuple3):
    """
    Есть три кортежа целых чисел необходимо найти элементы, 
    которые есть в каждом из кортежей и находятся в каждом 
    из кортежей на той же позиции.
    """
    result = []
    result_indx = []
    
    for i in range(len(random_tuple1)):
        for q in range(len(random_tuple2)):
            for w in range(len(random_tuple2)):
                if random_tuple1[i] == random_tuple2[q] == random_tuple3[w] and i == q == w:
                    result_indx.append(i)
                    result.append(random_tuple1[i])
       
    print("Позиція: ", result_indx, '\n'"Значення: ", result, '\n')

if __name__ == "__main__":

    random_tuple1 = tuple([randint(0, 2) for i in range(15)])
    random_tuple2 = tuple([randint(0, 2) for i in range(15)])
    random_tuple3 = tuple([randint(0, 2) for i in range(15)])

    print("Початковий кортеж 1: ", random_tuple1)
    print("Початковий кортеж 2: ", random_tuple2)
    print("Початковий кортеж 3: ", random_tuple3, '\n') 
    myfunk(random_tuple1, random_tuple2, random_tuple3)

