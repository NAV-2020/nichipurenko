"""
d = {}
print(type(d))

t = ()
print(type(t))



t = (2.3, "Hello", False)
tt = (2, 3, 'qwe', (1, 2, 3, 'qwe'), False)

t3 = (1, 2, [1, 2, 3], False)

print(t)
print(tt)
print(tt[2])

for i in range(len(t3[2])):
    t3[2][i]*= 2
print(t3)



from random import random

lst = []
for i in range(5):
    lst.append(randin)


a = ('ab', 'abcd', 'cde', 'abc', 'def')
b = input()
for  i in a:
    if b == i:
        print(True)
    else:
        print(False)
print(len(a))



F0 = 0
F1 = 1
number = 6

for i in range(2, number):
    a = F1
    F1 += F0
    F0 = 0

print("fib: ", F1)

"""

def fun(q):
    a = 1
    for i in range(1, q+1):
        a *= i
    return a

print("res: ", fun(5))

