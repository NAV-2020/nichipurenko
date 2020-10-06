"""
Створити генератор, який повертає значення помножене 
на 2 із зазначеного дапазону (2, 20) -> 4, 6, ...
"""

def generator(val1: int, val2: int):
    """Function - generator."""
    for i in range(val1, val2):
	    yield i*2

if __name__ == "__main__":

    val1 = 2
    val2 = 20
    
    for i in generator(val1, val2):
        print("Result: ", i)