'''
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.
'''
def readFile(myFaleRead: str) -> list:
    '''The function opens and reads a file'''
    with open(myFaleRead, 'r') as f:
        lines = f.readlines()
    return lines

def delString_writFile(myFaleWrite: str, lines:list) -> None:
    '''Function for deleting the last line and writing to a file'''
    with open(myFaleWrite, 'w') as f:
        f.writelines([item for item in lines[:-1]])
    
if __name__ == "__main__":
    
    
    myFaleRead = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text5.txt' 
    myFaleWrite = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text6.txt' 

    lines = readFile(myFaleRead)
    delString_writFile(myFaleWrite, lines)
    
