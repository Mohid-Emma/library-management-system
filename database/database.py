#database.py
import sqlite3
from   models import Book, Borrower
from   utils  import file_location, check_for_borrower


DB_PATH = file_location()

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    # =============================================================
    # Table Creation If not Exist
    # =============================================================

    def create_table(self) -> None:
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year INTEGER NOT NULL,
            available INTEGER DEFAULT 1,
            borrower_name TEXT )""")
        self.connection.commit()

    # =============================================================
    # Book Addition
    # =============================================================

    def add_book(self, book: Book) -> None:
        borrower_name = check_for_borrower(book)
        self.cursor.execute(""" INSERT INTO books 
        (title, author, pages, year, available, borrower_name) 
        VALUES (?, ?, ?, ?, ?, ?)""", 
        (book.title, book.author, book.pages, book.year, int(book.available), borrower_name))
        self.connection.commit()
        book.book_id = self.cursor.lastrowid

    # =============================================================
    # Fetch All Books
    # =============================================================

    def get_books(self) -> list[Book]:
        self.cursor.execute("""SELECT * FROM books""")
        rows =  self.cursor.fetchall()
        books: list[Book] = []
        for row in rows:
            book = Book(row[1], row[2], row[3], row[4], bool(row[5]), book_id=row[0])
            if row[6]:
                book.borrower = Borrower(row[6])
                book.available = False
            books.append(book)
        return books

    # =============================================================
    # Book Delection
    # =============================================================

    def delete_book(self, book: Book) -> None:
        self.cursor.execute("DELETE FROM books Where id=?", (book.book_id,))
        self.connection.commit()

    # =============================================================
    # Book Update
    # =============================================================

    def update_book(self, book: Book) -> None:
        borrower_name = check_for_borrower(book)
        self.cursor.execute(""" UPDATE books
        SET title=?, author=?, pages=?, year=?, available=?, borrower_name=? Where id=?""",
        (book.title, book.author, book.pages, book.year, int(book.available), borrower_name, book.book_id,))
        self.connection.commit()

    # =============================================================
    # Book Borrow
    # =============================================================

    def borrow_book(self, book: Book) -> None:
        borrower_name = check_for_borrower(book)
        self.cursor.execute(""" UPDATE books 
        SET available=?, borrower_name=? Where id=?""",
        (int(book.available), borrower_name, book.book_id,))
        self.connection.commit()

    # =============================================================
    # Book Return
    # =============================================================

    def return_book(self, book: Book) -> None:
        borrower_name = check_for_borrower(book)
        self.cursor.execute(""" UPDATE books 
        SET available=?, borrower_name=? Where id=?""",
        (int(book.available), borrower_name, book.book_id,))
        self.connection.commit()

    # =============================================================
    # Database Close
    # =============================================================

    def close(self) -> None:
        self.connection.close()
