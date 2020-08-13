import string
"""
print(string.ascii_letters)
print(string.hexdigits)
print(string.digits)
print(string.octdigits)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.whitespace)
print(string.printable)


print(dir(string))
for n in dir(string):
    if n.startswith('_'):
        continue
    v = getattr(string, n)
    if isinstance(v, str):
        print(f"{n} = {repr(v)}")




def foo(a: int) -> int:
    print(repr(a))
    print(a)
    return 2**2
foo('2')



patter = 'This is my favourite job!!1 IT Step'
print(repr(patter))
print(string.capwords(patter))

"""
leet = str.maketrans('qwertyuio', '123456789')
s = 'jhffjshfjkqwewewrytuyi skjdhfkj ksjdhf jkhdh'
print(s.translate(leet))






