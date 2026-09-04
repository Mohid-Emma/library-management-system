#book_form.py

import customtkinter as     ctk
from   models        import Book
from   config        import theme
from   tkinter       import messagebox
from   utils         import check_integer


class BookForm(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master, fg_color= theme.transparent)

        self.create_widget()

# =============================================================
# Widget Creation
# =============================================================

    def create_widget(self) -> None:

        self.grid_columnconfigure(0, weight=1)

        self.title_label  = self.create_label("Book Title", row=0)
        self.title_entry  = self.create_entry("Enter Book Title", row=1)

        self.author_label = self.create_label("Author", row=2)
        self.author_entry = self.create_entry("Enter Author", row=3)

        self.pages_label  = self.create_label("Pages", row=4)
        self.pages_entry  = self.create_entry("Enter Pages", row=5)

        self.year_entry   = self.create_entry("Enter Publication Year", row=7)
        self.year_label   = self.create_label("Publication Year", row=6)

        self.available_checkbox = ctk.CTkCheckBox(
            master        =  self, 
            text          = "Available", 
            font          = ("Segoe UI", 13, "bold"), 
            fg_color      = theme.success, 
            hover_color   = theme.success,
            border_color  = theme.text_muted,
            corner_radius = 6)
        self.available_checkbox.grid(row=8, column=0, padx=5, pady=(20,5))

# =============================================================
# Label Creation
# =============================================================

    def create_label(self, text : str, row :int) -> ctk.CTkFrame:

        label = ctk.CTkLabel(
            master        = self, 
            text          = text,
            text_color    = theme.text,
            font          = ("Segoe UI", 12, "bold"))
        label.grid(row=row, column=0, padx=5, pady=(8,4), sticky="w")
        return label

# =============================================================
# Entry Creation
# =============================================================

    def create_entry(self, placeholder : str, row : int) -> ctk.CTkEntry:

        entry = ctk.CTkEntry(
            master                 = self, 
            placeholder_text       = placeholder,
            height                 = 40,
            corner_radius          = 9,
            border_width           = 1,
            border_color           = theme.border,
            fg_color               = theme.background,
            text_color             = theme.text,
            placeholder_text_color = theme.text_muted,
            font                   = ("Segoe UI", 13))
        entry.grid(row=row, column=0, padx=5, pady=(0,8), sticky="ew")
        return entry

# =============================================================
# Entry Clear
# =============================================================

    def clear_entries(self) -> None:

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

    def fill_entries(self, book : Book) -> None:

        self.title_entry.insert( 0, book.title)
        self.author_entry.insert(0, book.author)
        self.pages_entry.insert( 0, str(book.pages))
        self.year_entry.insert(  0, str(book.year))

# =============================================================
# Get Book's Data from User
# =============================================================

    def get_book(self) -> None | Book:

        title     = self.title_entry.get().strip()
        author    = self.author_entry.get().strip()
        pages     = check_integer(self.pages_entry.get(), "Pages")
        year      = check_integer(self.year_entry.get(), "Year")
        available = bool(self.available_checkbox.get())

        if pages is None or year is None:
            return None
        try:
            book = Book(title, author, pages, year, available)
        except ValueError as error:
            messagebox.showerror("Invalid Input" ,str(error)+" "*100)
            return None
        return book

# =============================================================
# Disable/ Able of Checkbox During Edit Mode
# =============================================================

    def set_edit_mode(self, mode : bool) -> None:
        if mode:
            self.available_checkbox.deselect()
            self.available_checkbox.configure(state="disabled")  
        else:
            self.available_checkbox.configure(state="normal") 
