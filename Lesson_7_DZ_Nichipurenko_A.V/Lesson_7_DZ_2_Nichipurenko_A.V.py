'''
Задание 2
Пользователь вводит с клавиатуры некоторый текст,
после чего пользователь вводит список зарезервированных
слов. Необходимо найти в тексте все зарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст. 
'''

messag_e = input("Введіть текст: ")
messag_key = input("Введіть слова: ")

#messag_e = 'Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона.'
#messag_key = 'кортеж, часть, сам'

text_2 = ''


for text in messag_e.split(): # перебір тексту
    for text_1 in messag_key.split(', '): # перебір ключевих слів 
        if text_1 in text:
            text = text.upper() # верхній регістр
    text_2 += text + ' ' 

text_2 = text_2.rstrip()

print(text_2)

