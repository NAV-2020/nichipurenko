#a = 10
#b = -15
#a = abs(a)

#b = abs(b)
#print(b)

#def abs(a: int)
    #return a**2

#a = -20
#a = abs(a)
#print(a)


#def foo():
    #print("Hello")
    
#print(foo())
#print(foo)

#two = lambda : 2
#print(two())

#b = lambda x: x**2
#print(b(4))

#lst = [1, 2, 3, 4, 5]
#lst2 = map(lambda  x: x**2, lst)

#print(lst)
#print(lst2)

#a = [1, 2, 3, 4, 5, 6]
#b = filter(lambda x : x % 2 == 0, a) 
 
#print(list(b))


"""

a = [1, 2, 3, 4, 5, 6, True, False, "Hello", "Python"]
def foo(x):
    if type(x) == int:
        if x < 3 or x == 6:
            return True
    if type(x) == bool:
        if not x :
            return True
    if type(x) == str:
        if "n" in x:
            return True
    else:
        return False

b = filter(foo, a)
print(list(b))


#### Замикання

def outer(par):
    loc = par
    def inner():
        return loc
    return inner()
var = 1
a = outer(var)
print(a)


def makeclosere(a):
    loc = a
    def power(b):
        return b**a
    return power

cub = makeclosere (3)
print(cub(3))

"""



def mult(x):
    for i in x
        return (x*1)

if __name__ == "__main__":
    x = [i for i in range(1, 10)]
    a = mult (x)
    print(a)