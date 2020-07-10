
def my_centimeter(met_Var):
    """
    Приклад використання map():
    Конвертація: ментри в сантеметри.
    """
    return met_Var * 1000


print("Конвертація: ментри в сантеметри. \n") 
my_meter = [1.0, 7.5, 87.4, 2.5, 9]
print("Конвертація списку: ", my_meter, '\n')

result = list(map(my_centimeter, my_meter))

print ("Конвертований список: ", result)
 
