'''
Задание 3
Есть некоторый текст. Посчитайте в этом тексте количество предложений и 
выведите на экран полученный результат.
'''

text = input("Введіть текст : ")

#text = '''Українська мова – одна з найрозвиненіших у світі. Вона має величезний лексичний фонд, багату синоніміку.
#Наприклад, лелека, улюблений в Україні птах, має не лише цю назву. Він і чорногуз, і бусол, і гайстер, і бузько. 
#А яка різноманітність граматичних засобів, скільки зменшувально-пестливих форм: вітер – вітерець, 
#вітрець, вітрик, вітронько. А є й збільшені: вітрисько, вітрище, вітровій, вітрюган.'''

sentence = 0
for i in text:
    if ((i=='.') or (i=='!') or (i=='?')):
        sentence +=1
print('Кількість речень - ', sentence)