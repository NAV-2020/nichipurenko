"""
Есть некоторый текст. Посчитайте в этом тексте количество 
предложений и выведите на экран полученныйрезультат.
"""


def number_of_offers(text: int) -> int:
    sentence = 0
    for i in text:
        if ((i=='.') or (i=='!') or (i=='?')):
            sentence +=1
    return(sentence)

if __name__ == "__main__":

    TEXT = 'Текст'
    EXIT = 'Вихід'

    print("""
        Есть некоторый текст. Посчитайте в этом тексте количество 
        предложений и выведите на экран полученныйрезультат."""
    )

    while True:
        print("""
        Для виходу введіть -> Вихід
        Для введення тексту введіть -> Текст
        """)
      
        choice = input('Вибір: ')
        print()

        if choice == EXIT:
            break
        elif choice == TEXT:
            text = input("Введіть текст: ")
            print("-" * 40)
            print('Кількість речень - ', number_of_offers(text))
            print()
            input('Натисніть ENTER щоб продовжити...')