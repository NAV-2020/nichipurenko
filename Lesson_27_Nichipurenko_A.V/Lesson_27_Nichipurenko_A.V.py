"""
a = [3, 8, 12, 20]
aa = iter(a)
#print(a)
print(aa)
next(aa)
b = next(aa)
print(b)



class SimpIterator:
    def __iter__(self):
        return self
    def __init__(self,limit):
        self.limit = limit
        self.counter = 0
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter_1 = SimpIterator(3)

print(next(s_iter_1))
#for i in s_iter_1:
    #print(i)

"""

