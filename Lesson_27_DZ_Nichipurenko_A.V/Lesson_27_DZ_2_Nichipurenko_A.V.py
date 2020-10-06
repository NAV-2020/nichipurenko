"""
2. Написати ф-цію, яка переглядає файли в зазначеному каталозі 
(дивитися приклад в кінці файла). реалізувати за допомогою 
генераторів такі компоненти:
    - генерація множини імен файлів
    - генерація всіх строк зі всіх файлів
    - фільтрація строк на основі співставлення з абзацом

def emit_lines(pattern=None):
    lines = []
    for dir_path, dir_names, file_names in os.walk('test/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                for line in open(os.path.join(dir_path, file_name)):
                    if pattern in line:
                        lines.append(line)
    return lines
"""

import os

def gener_file_names(my_path: str, file_extens: str):
    """Multiple filename generator function."""
    for dir_path, dir_names, file_names in os.walk(my_path):
        for file_name in file_names:
            if file_name.endswith(file_extens):
                yield open(os.path.join(dir_path, file_name))

def iter_files(files):
    """Filename iteration function."""
    for fname in files:
        for line in fname:
            yield line

def iter_lines(lines, pattern):
    """String iteration function."""
    for line in lines:
        if pattern in line:
            yield line

if __name__ == "__main__":

    my_path = '/IT_School/nichipurenko/Lesson_27_DZ_Nichipurenko_A.V/test'
    val = "python"   
    file_extens = '.txt'

    ext_files = gener_file_names(my_path, file_extens)
    ext_file = iter_files(ext_files)
    lines = iter_lines(ext_file, val)
    
    print('*'*40)
    for line in lines:
        print(line)
    print('*'*40)