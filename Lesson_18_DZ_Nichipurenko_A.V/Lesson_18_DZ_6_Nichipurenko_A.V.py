'''
Дан текстовый файл. Найти и заменить в нем заданное слово. 
Что искать и на что заменять определяется пользователем.
'''
def readFile(myFale: str) -> str:
    '''The function opens and reads a file'''
    with open(myFale, 'r', encoding='utf-8') as f:
        result = f.read()
    return result

def word_replacement(lines: str, oldWord: str, newWord: str) -> str:
    '''Word count function'''
    if oldWord in lines:
        lines = lines.replace(oldWord, newWord)
    return lines

def writeText(res: str):
    '''The function of saving data to a file '''
    with open(file_name, "w") as f2:
        f2.write(res)
        

if __name__ == "__main__":

    myFale = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text5.txt'

    file_name = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text7.txt'

    #! oldWord = 'За'
    oldWord = input('Enter the old word: ')
    newWord = input('Enter the new word: ')
    
    lines = readFile(myFale)
    valueWord = word_replacement(lines, oldWord, newWord)
    writeText(valueWord)
    
