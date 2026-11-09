# controller.py

from tkinter import messagebox
from typing  import Any


class LibraryApp:
    def __init__(self, main_window, ui_compounds, database, library) -> None:


        self.current_book = None
        self.library = library(self, database)

        operation = {
            "add"     : self.add_book,
            "toolbar" : {"search" : self.search_books,"sort" : self.sort_books},
            "card"    : {"edit"   : self.edit_book,   "delete" : self.delete_book,
                         "return" : self.return_book, "borrow" : self.borrow_book},
            "close"   : self.library.close}

        self.main_window = main_window(ui_compounds, operation)
        self.refresh_books()

# =============================================================
# Book Addition
# =============================================================
    
    def add_book(self, mode) -> None:
        if mode == "addition":
            self.create_new_book()
        else:
            self.save_book_changes()

# Book Creation
    def create_new_book(self) -> None:
        book = self.main_window.book_data()
        if book is None:
            return
        
        if not self.library.add_book(book):
            self.set_status("Book already exists.")
            return
        
        self.main_window.form_clear()
        self.refresh_books()
        self.set_status(f"📚 '{book["title"]}' added.")

# Book Save
    def save_book_changes(self) -> None:
        updated_book = self.main_window.book_data()
        if updated_book is None:
            return
        
        self.library.edit_book(updated_book)
        self.refresh_books()
        self.set_status(f"✏️ '{updated_book["title"]}' is edited.")

# =============================================================
# Book Edition
# =============================================================
    
    def edit_book(self, book: dict[str, Any]) -> None:
        self.current_book = None
        self.current_book = book
        self.main_window.edit(book)
        self.set_status(f"✏️ '{book["title"]}' is edited.")

# =============================================================
# Book Delection
# =============================================================

    def delete_book(self, book: dict[str, Any]) -> None:
        self.current_book = None
    
        if not messagebox.askyesno("Delete Book", f" Delete '{book["title"]}'?\n"+" "*100):
            return
        if self.library.delete_book(book):
            self.refresh_books()
            self.set_status(f"🗑️ '{book["title"]}' deleted.")

# =============================================================
# Book Borrow
# =============================================================

    def borrow_book(self, book: dict[str, Any]) -> None:
        self.main_window.cancel_edit()
        borrower_name = self.main_window.dialog(book["title"])
        if borrower_name is None:
            return
        
        if self.library.borrow_book(book, borrower_name):
            self.refresh_books()
            self.set_status(f"📗 '{book["title"]} is Successfully Borrowed.")
        else:
            self.set_status(f"{book["title"]} is already borrowed.")

# =============================================================
# Book Return
# =============================================================

    def return_book(self, book: dict[str, Any]) -> None:
        self.main_window.cancel_edit()
        if self.library.return_book(book):
            self.refresh_books()
            self.set_status(f"📗 Returned '{book["title"]}'.")
        else:
            self.set_status(f"'{book["title"]}' is already available.")

# =============================================================
# Book Sort
# =============================================================

    def sort_books(self, choice : str) -> None:

        sort_options = {
            "Title (A-Z)"      : lambda b: b.title.lower(),
            "Title (Z-A)"      : lambda b: b.title.lower(),
            "Author"           : lambda b: b.author.lower(),
            "Year (Newest)"    : lambda b: b.year,
            "Year (Oldest)"    : lambda b: b.year,
            "Pages (Smallest)" : lambda b: b.pages,
            "Pages (Largest)"  : lambda b: b.pages,
            "Available"        : lambda b: (not b.available, b.title.lower()),
            "Borrowed"         : lambda b: (b.available, b.title.lower())}

        key = sort_options.get(choice)
        if key is None:
            return
        reverse = choice in ("Title (Z-A)", "Year (Newest)","Pages (Largest)")
        self.database.books.sort(key=key, reverse=reverse)
        self.refresh_books()

# =============================================================
# Search for Book
# =============================================================

    def search_books(self, query : str) -> None:
        query = query.strip().lower()
        books = [book for book in self.database.books if self.matches_search(book, query)]
        self.book_list.display_books(books)

    def matches_search(self, book, query):
        borrower = ""
        if book.borrower:
            borrower = book.borrower.name.lower()
        return any(
            [query in book.title.lower(), 
            query in book.author.lower(),
            query in str(book.year), query in borrower , 
            query in ("available" if book.available else "borrowed")])

# =============================================================
# Display Currrent Action
# =============================================================

    def refresh_books(self) -> None:
        self.main_window.display_books(self.library.load())

    def set_status(self, message : str) -> None:
        self.main_window.set_status(message)

    def run(self) -> None:
        self.main_window.mainloop()