'''
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.
'''
def readFile(text: str) -> list:
    '''The function opens and reads a file'''
    with open(text, 'r', encoding='utf-8') as val:
        scroll = val.readlines()
    return scroll

def mismatched_strings1(txt_1: list, txt_2: list, list_lines: list) -> list:
    '''Find mismatched lines in files '''
    for sample in txt_1:
        if sample not in txt_2:
            list_lines.append(sample)
        else:
            continue 
    return list_lines  

def del_whitespace_characters(del_gaps: list) -> list:
    '''Function to remove whitespace at the end of a line'''
    res = [line.rstrip() for line in del_gaps]
    return res


if __name__ == "__main__":

    fileOne = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text1.txt'
    fileTwo = 'F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text2.txt'
    
    text_1 = readFile(fileOne)
    text_2 = readFile(fileTwo)

    list_lines1 = []
    list_lines2 = []
    
    list1 = mismatched_strings1(text_1, text_2, list_lines1)
    list2 = mismatched_strings1(text_2, text_1, list_lines2)

    print()
    print('Mismatched lines in files 1: ', del_whitespace_characters(list1))
    print('Mismatched lines in files 2: ', del_whitespace_characters(list2), '\n')
