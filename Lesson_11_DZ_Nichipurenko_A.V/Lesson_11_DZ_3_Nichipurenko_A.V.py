
def my_fun(var):
    """
    Приклад використання filter():
    Функція поверне з ітеруємого списку об`єкт при яких
    умова буде вірна. Тобто поверне ті слова в яких
    буде об`єкт 'o' .
    """
    return 'o' in var.lower()


print("""
    Функція поверне з ітеруємого списку об`єкт при яких
    умова буде вірна. Тобто поверне ті слова в яких
    буде об`єкт 'o' .\n""")
myLst = ['help', 'Hello', 'Python', 'green', 'power']
print('Список ітеруємих об`єктів: ', myLst, '\n')

result = list(filter(my_fun, myLst))
print('Результат: ', result)

