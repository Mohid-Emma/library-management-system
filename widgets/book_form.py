#book_form.py

import customtkinter as     ctk
from   models        import Book
from   tkinter       import messagebox
from   utils         import check_integer

class BookForm(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title_entry        = self.create_entry("Book Title")
        self.author_entry       = self.create_entry("Author")
        self.pages_entry        = self.create_entry("Pages")
        self.year_entry         = self.create_entry("Publication Year")
        self.available_checkbox = ctk.CTkCheckBox(self, text="Available", font=("Helvetica", 18), fg_color="green", hover_color="green")
        self.available_checkbox.pack(padx=15, pady=15, expand="True")

    # =============================================================
    # Entry Creation
    # =============================================================

    def create_entry(self, placeholder):

        entry = ctk.CTkEntry(self, placeholder_text= placeholder, font=("Helvetica", 15), corner_radius=10)
        entry.pack(padx=20, pady=20, expand="True", fill="both")
        return entry

    # =============================================================
    # Entry Creation
    # =============================================================

    def clear_entries(self):

        entries = [
            self.title_entry, 
            self.author_entry,
            self.pages_entry, 
            self.year_entry]
        for entry in entries:
            entry.delete(0, "end")
        self.available_checkbox.deselect()

    # =============================================================
    # Fill the Entries with Book's Data
    # =============================================================

    def fill_entries(self, book):

        self.title_entry.insert(0, book.title)
        self.author_entry.insert(0, book.author)
        self.pages_entry.insert(0, str(book.pages))
        self.year_entry.insert(0, str(book.year))

    # =============================================================
    # Get Book's Data from User
    # =============================================================

    def get_book(self):

        title     = self.title_entry.get()
        author    = self.author_entry.get()
        pages     = check_integer(self.pages_entry.get(), "Pages")
        year      = check_integer(self.year_entry.get(), "Year")
        available = bool(self.available_checkbox.get())

        if pages is None or year is None:
            return
        try:
            book = Book(title, author, pages, year, available)
        except ValueError as error:
            messagebox.showerror("Invalid Input" ,str(error))
            return
        return book

    # =============================================================
    # Disable/ Able of Checkbox During Edit Mode
    # =============================================================

    def set_edit_mode(self, mode):
        if mode:
            self.available_checkbox.deselect()
            self.available_checkbox.configure(state="disabled")  
        else:
            self.available_checkbox.configure(state="normal") 
