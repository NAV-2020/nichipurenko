
"""
Создайте программу «Книжная коллекция». Нужно
хранить информацию о книгах: автор, название книги,
жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удаления, 
поиска, замены данных. Используйте словарь для
хранения информации.
"""

import pprint

def get_book(book: list) -> list:
    return book

def print_result(*args) -> None:
    for element in args:
        #print(element)
        pprint.pprint(element, width=1)
        input('Press to continue...')

def add_book(author: str, book_title: str, genre: str, year_of_issue: str,
                            number_of_pages: str, publishing_house: str) -> dict:
    global BOOK
    book = {
        "Author": author,
        "Book title": book_title,
        "Genre": genre,
        "Year of issue": year_of_issue,
        "Number of pages": number_of_pages,
        "Publishing house": publishing_house
    }
    BOOK.append(book)
    return book

def del_book(author: str) -> dict:
    global BOOK
    deleted_book = {}
    for index, book in enumerate(BOOK):
        if book['Author'] == author:
            deleted_book = book
            del(BOOK[index])
            return deleted_book

def search_book(author: str) -> dict:
    global BOOK
    for book in BOOK:
        if book['Author'] == author:
            return book
    return f"Book {author} does not exist\n"

def update_book(author: str) -> dict:
    global BOOK
    for index, book in enumerate(BOOK):

        if book['Author'] == author:
            author = book["Author"]
            book_title = book['Book title']
            genre = book['Genre']
            year_of_issue = book['Year of issue']
            number_of_pages = book['Number of pages']
            publishing_house = book['Publishing house']
             
            new_author = input(f"Enter author ({author} - default): ")
            new_book_title = input(f"Enter the title of the book ({book_title} - default): ")
            new_genre = input(f"Enter genre ({genre} - default): ")
            new_year_of_issue = input(f"Enter middle growth ({year_of_issue} - default): ")
            new_number_of_pages = input(f"Enter the number of pages ({number_of_pages} - default): ")
            new_publishing_house = input(f"Enter publisher ({publishing_house} - default): ")

            if new_author:
                book['Author'] = new_author
            if new_book_title:
                book['Book title'] = new_book_title
            if new_genre:
                book['Genre'] = new_genre
            if new_year_of_issue:
                book['Year of issue'] = new_year_of_issue
            if new_number_of_pages:
                book['Number of pages'] = new_number_of_pages
            if new_publishing_house:
                book['Publishing house'] = new_publishing_house
            return book



if __name__ == "__main__":
    
    BOOKS_LIST = 'list'    # список книг
    ADD_BOOK = 'add'       # добавить
    DEL_BOOK = 'delete'    # удалить
    SEARCH_BOOK = 'search' # поиск
    UPDATE_BOOK = 'update' # обновить
    EXIT = 'q'             # выход
    BOOK = []

    print("""
    Создайте программу «Книжная коллекция». Нужно
    хранить информацию о книгах: автор, название книги,
    жанр, год выпуска, количество страниц, издательство.
    Требуется реализовать возможность добавления, удаления, 
    поиска, замены данных. Используйте словарь для
    хранения информации.
    """
    )

    while True:
        print(f'''
        Choices:
        BOOKS_LIST -> {BOOKS_LIST}
        ADD_BOOK -> {ADD_BOOK}
        DEL_BOOK -> {DEL_BOOK}
        SEARCH_BOOK -> {SEARCH_BOOK}
        UPDATE_BOOK -> {UPDATE_BOOK}
        EXIT -> {EXIT}
        ---------------------
        ''')
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == BOOKS_LIST:
            book = get_book(BOOK)
            print_result(book)

        elif choice == ADD_BOOK:
            author = input('Enter author: ') # автор
            book_title = input('Enter the title of the book: ') # название
            genre = input('Enter genre: ') # жанр
            year_of_issue = input('Enter year of manufacture: ') # год выпуска
            number_of_pages = input('Enter the number of pages: ') # количество страниц
            publishing_house = input('Enter publisher: ') # Издательство

            book = add_book(
                author = author,
                book_title = book_title,
                genre = genre,
                year_of_issue = year_of_issue,
                number_of_pages =  number_of_pages,
                publishing_house = publishing_house
            )
            print_result(book)

        elif choice == DEL_BOOK:
            author = input("Enter author: ")
            book = del_book(author = author)
            print_result(book)

        elif choice == SEARCH_BOOK:
            author = input("Enter author: ")
            book = search_book(author = author)
            print_result(book)

        elif choice == UPDATE_BOOK:
            author = input("Enter author: ")
            book = update_book(author = author)
            if book != None:  
                print_result(book)
