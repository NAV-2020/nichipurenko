'''
Задание 1
Пользователь вводит с клавиатуры строку. Проверьте
является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
слева направо и справа налево. Например, кок; А роза
упала на лапу Азора; доход; А буду я у дуба.
'''

messag_e = input("Введіть строку: ")
message_1 = messag_e.replace(" " , "") 
message_1 = message_1.lower()
if message_1 == message_1[::-1]:
   print(messag_e, ' - палиндром')
else:
    print(messag_e, ' - не палиндром')
