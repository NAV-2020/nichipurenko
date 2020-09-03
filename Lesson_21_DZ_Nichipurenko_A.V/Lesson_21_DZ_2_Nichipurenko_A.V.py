'''
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
'''

import random

class Book:
    
    numberBook = 0
    genre = ['poetry', 'adventures', 'fantastic', 'detective']

    def __init__(self,
                book_title: str, 
                year: int,
                publisher: str,
                author: str,
                genre: str = '',
                price: float = 0.0):
        """Initializes the book data attributes"""
        self.book_title = book_title
        self.year = year
        self.publisher = publisher
        self.author = author
        self.price = price
        self.genre = genre

        Book.numberBook += 1

    def __str__(self):
        '''Returns data'''
        return f'''
        Book title: {self.book_title} 
        Year of issue: {self.year} 
        Bublisher: {self.publisher} 
        Author: {self.author} 
        Price: {self.price}
        Genre: {self.genre}
        '''

    def __del__(self):
        """Destructor call, when the object(Book) is removed from the list"""
        print(f'Book {self.book_title} removed from the list!')
        Book.numberBook -= 1
        if Book.numberBook == 0:
            print("There are no Books in the list!")
        else:
            print(f"Left: {Book.numberBook}.")

    def book_price(self, book_val: float) -> None:
        '''Method for entering engine displacement.'''
        try:
            self.price = float(book_val)
        except ValueError as e:
            #print(e)
            print("Error: please enter a number of float")

    def set_genre(self) -> str:
        '''The method of random selection of the publisher of the book.'''
        self.genre = random.choice(Book.genre)
        return self.genre

if __name__ == "__main__":
   
    my_book1 = Book('"Dance with dragons"', 2009, 'Rainbow','George R.')
    my_book1.set_genre()
    my_book2 = Book('"Dance"', 2019, 'Rainbow','George R.')
    my_book2.set_genre()

    book_val = input("Enter engine volume book 1: ")
    my_book1.book_price(book_val)
    
    book_val = input("Enter engine volume book 2: ")
    my_book2.book_price(book_val)
    
    print(my_book1)
    print(my_book2)

    print('Number of books: ', Book.numberBook)
    #del my_book2
    #print('Number of books: ', Book.numberBook)
    output = input('Press to continue...')
