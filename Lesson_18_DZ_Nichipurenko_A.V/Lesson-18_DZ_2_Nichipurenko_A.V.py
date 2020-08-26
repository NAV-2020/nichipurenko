'''
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
    Количество символов;
    Количество строк;
    Количество гласных букв;
    Количество согласных букв;
    Количество цифр.
'''

def write_analytics(file_name: str, 
                    number_of_lines: int,
                    number_of_chars: int, 
                    number_of_vowels: int,
                    number_of_cosonants: int,
                    number_of_digits: int) -> None:
    '''The function of saving data to a file '''

    with open(file_name, "w") as f2:
        f2.write(f"Number of lines: {number_of_lines}\n")
        f2.write(f"Number of chars: {number_of_chars}\n")
        f2.write(f"Number of vowels: {number_of_vowels}\n")
        f2.write(f"Number of consonants: {number_of_cosonants}\n")
        f2.write(f"Number of digits: {number_of_digits}\n")
       
def get_number_of_lines() -> int:
    '''Line counting function'''

    with open("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text3.txt", "r") as f1:
        number_of_lines = 0
        lines = f1.readlines()
        for line in lines:
            if line != '\n':
                number_of_lines += 1
    return number_of_lines

def get_number_of_chars() -> int:
    '''Character counting function'''

    with open("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text3.txt", "r") as f1:
        text = f1.read()
    return len(text)


def get_the_number_of_vowels() -> int:
    '''Vowel counting function'''

    voice_letters =  ('а', 'е', 'и', 'і', 'о', 'у', 'я', 'ю', 'є', 'ї')
    vowel = []
    with open("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text3.txt", "r", 
                encoding='utf-8') as f1:
        text = f1.read()
        for char in text:
            if char in voice_letters:
                vowel.append(char)
    return len(vowel)

def get_the_number_of_consonants()  -> int: #получить количество согласных букв
    '''The function of counting the number of consonants'''
    
    voiced_let = ('б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 
                        'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь')
    consonant = []             
    with open("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text3.txt", "r", 
                encoding='utf-8') as f1:
        text = f1.read()
        for char in text:
            if char in voiced_let:
                consonant.append(char)
        #consonant = [char for char in text if char in voiced_let]
    return len(consonant)

def get_number_of_digits() -> int:
    '''Digit counting function'''

    with open("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text3.txt", "r") as f1:
        text = f1.read()
        digits = [char for char in text if char.isdigit()]
    return len(digits)

if __name__ == "__main__":
    
    number_of_lines = get_number_of_lines()
    number_of_chars = get_number_of_chars()
    number_of_vowels = get_the_number_of_vowels()
    number_of_cosonants = get_the_number_of_consonants()
    number_of_digits = get_number_of_digits()
    write_analytics("F:\\IT_School\\nichipurenko\\Lesson_18_DZ_Nichipurenko_A.V\\Text4.txt", 
                            number_of_lines, number_of_chars, number_of_vowels, 
                            number_of_cosonants, number_of_digits)



