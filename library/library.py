#library.py
from models import Book, Borrower
    
class Library:
    def __init__(self, db) -> None:
        self.books : list[Book] = []
        self.db = db

    def find_book(self, title : str) -> Book | None:
        for book in self.books:
            if book.title.casefold() == title.casefold():
                return book
        return None

    def add_book(self, book : Book) -> bool:
        if self.find_book(book.title):
            return False
        self.books.append(book)
        self.db.add_book(book)
        return True

    def delete_book(self, book : Book):
        if book in self.books:
            self.books.remove(book)
            self.db.delete_book(book)
            return True
        return False

    def borrow_book(self, book: Book, borrower: Borrower) -> bool:
        if book.borrow(borrower):
            self.db.borrow_book(book)
            return True
        return False

    def return_book(self, book: Book):
        if book.return_book():
            self.db.return_book(book)
            return True
        return False

    def load(self) -> None:
        self.books =  self.db.get_books()

    def update_book(self, book: Book):
        self.db.update_book(book)

