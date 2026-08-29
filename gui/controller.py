# controller.py

from  tkinter         import messagebox
from .borrower_dialog import BorrowerDialog


class Controller:
    def __init__(self, app, library, book_form, book_list, toolbar, statusbar):
        self.app          = app
        self.library      = library
        self.book_form    = book_form
        self.book_list    = book_list
        self.toolbar      = toolbar
        self.status_bar   = statusbar
        self.current_book = None

    # =============================================================
    # Loading Book's Data 
    # =============================================================

        self.library.load()

    # =============================================================
    # Modules Assignation
    # =============================================================

    def set_callback(self, on_set_edit_mode):
        self.on_set_edit_mode = on_set_edit_mode

    # =============================================================
    # Book Addition
    # =============================================================
    
    def add_book(self):
        if self.current_book is None:
            self.create_new_book()
        else:
            self.save_book_changes()
    # =============================================================
    # Book Creation
    # =============================================================

    def create_new_book(self):
        book = self.book_form.get_book()
        if book is None:
            return
        
        if not self.library.add_book(book):
            self.set_status("Book already exists.")
            return
        self.book_form.clear_entries()
        self.refresh_books()
        self.set_status(f"📚 '{book.title}' added.")

    # =============================================================
    # Book Save
    # =============================================================

    def save_book_changes(self):
        updated_book = self.book_form.get_book()
        if updated_book is None:
            return
        
        self.current_book.update(updated_book)
        self.library.update_book(self.current_book)
        title = self.current_book.title

        self.reset_form()
        self.refresh_books()
        self.set_status(f"✏️ '{title}' updated.")

    # =============================================================
    # Book Edition
    # =============================================================
    
    def edit_book(self, book):
        self.current_book = book
        self.book_form.clear_entries()
        self.book_form.fill_entries(book)
        self.book_form.set_edit_mode(True)
        self.on_set_edit_mode(True)
        self.app.title(f"Editing - {book.title}")

    # =============================================================
    # Edit Mode Cancel 
    # =============================================================
    
    def cancel_edit(self):
        self.reset_form()
        self.set_status("Edit cancelled.")

    # =============================================================
    # Clear Entries
    # =============================================================

    def reset_form(self):
        self.current_book = None
        self.book_form.clear_entries()
        self.book_form.set_edit_mode(False)
        self.on_set_edit_mode(False)

    # =============================================================
    # Book Delection
    # =============================================================

    def delete_book(self, book):
        self.cancel_edit()
    
        if not messagebox.askyesno("Delete Book", f" Delete '{book.title}'?\n"+" "*100):
            return
        if self.library.delete_book(book):
            self.refresh_books()
            self.set_status(f"🗑️ '{book.title}' deleted.")

    # =============================================================
    # Book Borrow
    # =============================================================

    def borrow_book(self, book):
        self.cancel_edit()
        dialog = BorrowerDialog(self.app, book.title)
        self.app.wait_window(dialog)
        borrow = dialog.get_result()
        if borrow is None:
            return
        if self.library.borrow_book(book, borrow):
            self.refresh_books()
            self.set_status(f"📗 '{book.title} is Successfully Borrowed.")
        else:
            self.set_status(f"{book.title} is already borrowed.")

    # =============================================================
    # Book Return
    # =============================================================

    def return_book(self, book):
        self.cancel_edit()
        if self.library.return_book(book):
            self.refresh_books()
            self.set_status(f"📗 Returned '{book.title}'.")
        else:
            self.set_status(f"'{book.title}' is already available.")

    # =============================================================
    # Book Sort
    # =============================================================

    def sort_books(self, choice):

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
        self.library.books.sort(key=key, reverse=reverse)
        self.refresh_books()

    # =============================================================
    # Search for Book
    # =============================================================

    def search_books(self, query):
        query = query.strip().lower()
        books = [book for book in self.library.books if self.matches_search(book, query)]
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
    # Book's Update
    # =============================================================

    def refresh_books(self):
        self.book_list.display_books(self.library.books)

    # =============================================================
    # Display Currrent Action
    # =============================================================

    def set_status(self, message):
        self.status_bar.set_status(message)
