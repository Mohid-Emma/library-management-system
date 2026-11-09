# database.py

import sqlite3
from typing import Any
from utils import file_location


DB_PATH = file_location()

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    # =============================================================
    # Table Creation If not Exist
    # =============================================================

    def create_table(self) -> None:
        self.cursor.execute(
            """ CREATE TABLE IF NOT EXISTS books(
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

    def add_book(self, book: dict[str, Any]) -> bool:
        self.cursor.execute(""" INSERT INTO books 
        (title, author, pages, year, available, borrower_name) 
        VALUES (?, ?, ?, ?, ?, ?)""", 
        (book["title"], book["author"], book["pages"], book["year"], int(book["available"]), book["borrower"]))
        self.connection.commit()
        book["book_id"] = self.cursor.lastrowid
        return True

    # =============================================================
    # Book Edition
    # =============================================================

    def update_book(self, book: dict[str, Any]) -> None:
        self.cursor.execute(""" UPDATE books
        SET title=?, author=?, pages=?, year=?, available=?, borrower_name=? Where id=?""",
        (book["title"], book["author"], book["pages"], book["year"], int(book["available"]), book["borrower"], book["book_id"]))
        self.connection.commit()

    # =============================================================
    # Fetch All Books
    # =============================================================

    def fetch_books(self) -> list[dict[str, Any]]:
        self.cursor.execute("""SELECT * FROM books""")
        rows =  self.cursor.fetchall()
        books = []
        for row in rows:
            books.append({
            "book_id"  : row[0],
            "title"    : row[1], 
            "author"   : row[2], 
            "pages"    : row[3], 
            "year"     : row[4], 
            "available": bool(row[5]), 
            "borrower" : row[6] if row[0] else None})
        return books

    # =============================================================
    # Book Delection
    # =============================================================

    def delete_book(self, book: dict[str, Any]) -> None:
        self.cursor.execute(
        "DELETE FROM books Where id=?", 
        (book["book_id"],))
        self.connection.commit()

    # =============================================================
    # Book Borrow
    # =============================================================

    def borrow_book(self, book: dict[str, Any]) -> None:
        self.cursor.execute(
        """ UPDATE books 
        SET available=?, borrower_name=? Where id=?""",
        (int(book["available"]), book["borrower"], book["book_id"]))
        self.connection.commit()

    # =============================================================
    # Book Return
    # =============================================================

    def return_book(self, book: dict[str, Any]) -> None:
        self.cursor.execute(
        """ UPDATE books 
        SET available=?, borrower_name=? Where id=?""",
        (int(book["available"]), book["borrower"], book["book_id"]))
        self.connection.commit()

    # =============================================================
    # Database Close
    # =============================================================

    def close(self) -> None:
        self.connection.close()
