'''
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.
'''
def readFile(myFale: str) -> str:
    '''The function opens and reads a file'''
    with open(myFale, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return str(lines)


def word_counter(word: str, lines: list):
    '''Word count function'''
    valueWord = lines.count(word)
    return valueWord

if __name__ == "__main__":
    
    myFale = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text5.txt'

    #! word = 'За'
    word = input('Enter the word: ')
    
    lines = readFile(myFale)
    
    print("Result: ", word_counter(word, lines))
