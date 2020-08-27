'''
Дан текстовый файл. Найти длину самой длинной
строки.
'''
def readFile(myFale: str) -> list:
    '''The function opens and reads a file'''
    with open(myFale, 'r') as f:
        lines = f.readlines()
    return lines

def long_line(lines: list) -> int:
    '''Line length counting function'''
    longest_string = []
    for elem in lines:
        for ls in elem:
            if len(ls) > len(longest_string):
                longest_string = elem
        return len(longest_string)

if __name__ == "__main__":
    
    myFale = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text5.txt'

    lines = readFile(myFale)
    print()
    print("Result: ", long_line(lines),'\n')