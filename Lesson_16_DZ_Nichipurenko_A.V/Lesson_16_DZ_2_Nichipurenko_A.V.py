"""
Создайте программу «Англо-французский словарь».
Нужно хранить слово на английском языке и его перевод
на французский. Требуется реализовать возможность добавления, 
удаления, поиска, замены данных. Используйте
словарь для хранения информации.
"""
import pprint

def get_english_french_vocab(english_french_vocab: list) -> list:
    return english_french_vocab

def print_result(*args) -> None:
    for element in args:
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_words(english: str, french: str) -> dict:
    global ENGLISH_FRENCH_VOCAB
    english_french_vocab = {
        "English": english,
        "French": french
    }
    ENGLISH_FRENCH_VOCAB.append(english_french_vocab)
    return english_french_vocab

def del_words(english: str) -> dict:
    global ENGLISH_FRENCH_VOCAB
    deleted_english_french_vocab = {}
    for index, english_french_vocab in enumerate(ENGLISH_FRENCH_VOCAB):
        if english_french_vocab['English'] == english:
            deleted_english_french_vocab = english_french_vocab
            del(ENGLISH_FRENCH_VOCAB[index])
            return deleted_english_french_vocab

def search_words(english: str) -> dict:
    global ENGLISH_FRENCH_VOCAB
    for english_french_vocab in ENGLISH_FRENCH_VOCAB:
        if english_french_vocab['English'] == english:
            return english_french_vocab
    return f"The word {english} does not exist\n"

def update_words(english: str) -> dict:
    global ENGLISH_FRENCH_VOCAB
    for index, english_french_vocab in enumerate(ENGLISH_FRENCH_VOCAB):

        if english_french_vocab['English'] == english:
            english = english_french_vocab["English"]
            french = english_french_vocab["French"]

            new_english = input(f"Enter English word ({english} - default): ")
            new_french = input(f"Enter French word ({french} - default): ")

            if new_english:
                english_french_vocab['English'] = new_english
            if new_french:
                english_french_vocab['French'] = new_french
            return english_french_vocab




if __name__ == "__main__":
    
    ENGLISH_FRENCH_VOCAB_LIST = 'list'  # список слов
    ADD_WORDS = 'add'                   # добавить
    DEL_WORDS = 'delete'                # удалить
    UPDATE_WORDS = 'update'             # обновить
    SEARCH_WORDS = 'search'             # поиск
    EXIT = 'q'                          # выход
    ENGLISH_FRENCH_VOCAB = []

    print("""
    Создайте программу «Англо-французский словарь».
    Нужно хранить слово на английском языке и его перевод
    на французский. Требуется реализовать возможность добавления, 
    удаления, поиска, замены данных. Используйте
    словарь для хранения информации.
    """

    )

    while True:
        print(f'''
        Choices:
        ENGLISH_FRENCH_VOCAB_LIST -> {ENGLISH_FRENCH_VOCAB_LIST}
        ADD_WORDS -> {ADD_WORDS}
        DEL_WORDS -> {DEL_WORDS}
        UPDATE_WORDS -> {UPDATE_WORDS}
        SEARCH_WORDS -> {SEARCH_WORDS}
        EXIT -> {EXIT}
        ---------------------
        ''')
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == ENGLISH_FRENCH_VOCAB_LIST:
            english_french_vocab = get_english_french_vocab(ENGLISH_FRENCH_VOCAB)
            print_result(english_french_vocab)

        elif choice == ADD_WORDS:
            english = input('Enter an english word: ') # фамилие
            french = input('Enter an french word: ') # имя
            english_french_vocab = add_words(
                english = english,
                french = french
            )
            print_result(english_french_vocab)

        elif choice == DEL_WORDS:
            english = input("Enter the English word to delete: ")
            english_french_vocab = del_words(english = english)
            print_result(english_french_vocab)

        elif choice == SEARCH_WORDS:
            english = input("Enter the English word: ")
            english_french_vocab = search_words(english = english)
            print_result(english_french_vocab)

        elif choice == UPDATE_WORDS:
            english = input("Enter English words: ")
            english_french_vocab = update_words(english = english)
            if english_french_vocab != None:  
                print_result(english_french_vocab)
