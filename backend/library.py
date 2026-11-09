# library.py
from typing import Any

    
class Library:
    def __init__(self, master, database) -> None:
        self.books: list[dict[str, Any]] = []
        self.database = database()
        self.database.create_table()
        self.current_mode = None


# =============================================================
# Book Find
# =============================================================

    def find_book(self, title: str) -> dict[str, Any] | None:
        for book in self.books:
            if book["title"].casefold() == title.casefold():
                return book
        return None
    
# =============================================================
# Book Addition
# =============================================================

    def add_book(self, book: dict[str, Any]) -> bool:
        if self.find_book(book["title"]):
            return False
        if not self.database.add_book(book):
            return False
        return True

    def edit_book(self, book: dict[str, Any]) -> bool:
        if self.find_book(book["title"]):
            return False
        self.database.update_book(book)
        return True

# =============================================================
# Book Delection
# =============================================================

    def delete_book(self, book: dict[str, Any]) -> bool:
        if book in self.books:
            self.database.delete_book(book)
            return True
        return False

# =============================================================
# Book Borrow
# =============================================================

    def borrow_book(self, book: dict[str, Any], borrower: str) -> bool:
        if book["available"]:
            book.update({
                "available": False,
                "borrower" : borrower})
            self.database.borrow_book(book)
            return True
        return False
    
# =============================================================
# Book Retuen
# =============================================================

    def return_book(self, book: dict[str, Any]) -> bool:
        if not book["available"]:
            book.update({
                "available": True,
                "borrower" : None})
            self.database.return_book(book)
            return True
        return False
    
# =============================================================
# Loading Book's Data
# =============================================================

    def load(self) -> list[dict[str, Any]]:
        self.books =  self.database.fetch_books()
        return self.books
    
# =============================================================
# Close Databse
# =============================================================

    def close(self) -> None:
        self.database.close()

