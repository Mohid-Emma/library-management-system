# book_form.py

import customtkinter as ctk
from config  import theme
from typing  import Any
from utils   import check_integer


class BookForm(ctk.CTkFrame):
    def __init__(self, master, operation) -> None:
        super().__init__(master, corner_radius = 15, border_width = 1, fg_color = theme.surface, border_color = theme.border)

        self.current_mode = "addition"
        self.current_book = None
        self.operation    = operation

        self.create_layout()
        self.create_title()
        self.create_widgets()
        self.create_button()

# =============================================================
# Create GUI/UI Compounds
# =============================================================

    def create_layout(self) -> None:
        self.grid_columnconfigure(0, weight=1)

    def create_title(self)-> None:
        self.form_title = ctk.CTkLabel(
            master     = self,
            text       = "Book Addition",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text)
        
        self.form_title.grid(row=0, column=0, padx=20, pady=(20,10), sticky="w")

    def create_label(self, text: str, row: int) -> ctk.CTkFrame:

        label = ctk.CTkLabel(
            master        = self, 
            text          = text,
            text_color    = theme.text,
            font          = ("Segoe UI", 12, "bold"))
        label.grid(row=row, column=0, padx=20, pady=(8,4), sticky="w")
        return label

    def create_entry(self, placeholder: str, row: int) -> ctk.CTkEntry:

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
        entry.grid(row=row, column=0, padx=20, pady=(0,8), sticky="ew")
        return entry
    
    def create_widgets(self) -> None:

        self.grid_columnconfigure(0, weight=1)

        self.title_label  = self.create_label("Book Title", row=1)
        self.title_entry  = self.create_entry("Enter Book Title", row=2)

        self.author_label = self.create_label("Author", row=3)
        self.author_entry = self.create_entry("Enter Author", row=4)

        self.pages_label  = self.create_label("Pages", row=5)
        self.pages_entry  = self.create_entry("Enter Pages", row=6)

        self.year_label   = self.create_label("Publication Year", row=7)
        self.year_entry   = self.create_entry("Enter Publication Year", row=8)

        self.available_checkbox = ctk.CTkCheckBox(
            master        =  self, 
            text          = "Available", 
            font          = ("Segoe UI", 13, "bold"), 
            fg_color      = theme.success, 
            hover_color   = theme.success,
            border_color  = theme.text_muted,
            corner_radius = 6)
        self.available_checkbox.grid(row=9, column=0, padx=5, pady=(20,5))

    def create_button(self) -> None:

        self.button_frame = ctk.CTkFrame(
            master   = self,
            fg_color = theme.transparent)

        self.button_frame.grid(row=10, column=0, padx=20, pady=(10, 20), sticky="ew")

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        # Cancel
        self.cancel_button = ctk.CTkButton(
            master        = self.button_frame, 
            text          = "Cancel",   
            height        = 42,
            corner_radius = 10,
            command       = self.cancel,
            fg_color      = theme.surface_light,
            hover_color   = theme.border, 
            font          = ("Segoe UI", 13, "bold"))

        self.cancel_button.grid(row=0, column=0, padx=10, sticky="ew")

        # Addition
        self.add_button = ctk.CTkButton(
            master        = self.button_frame, 
            text          = "Add Book", 
            height        = 42,
            corner_radius = 10,
            command       = lambda: self.operation(self.current_mode),
            fg_color      = theme.accent,
            hover_color   = theme.accent_hover, 
            font          = ("Segoe UI", 13, "bold"))

        self.add_button.grid(row=0, column=1, padx=10, sticky="ew")
    
# =============================================================
# Cancel Command
# =============================================================

    def cancel(self) -> None:
        if self.current_mode != "addition":
            self.mode_change("addition")
        self.form_clear()

# =============================================================
# Mode Change
# =============================================================

    def mode_change(self, mode: str) -> None:
        if mode == "addition":
            self.form_title.configure(text="Book Addition")
            self.add_button.configure(text="Add Book")
            self.available_checkbox.configure(state="normal")
            self.current_mode = "addition"
        else:
            self.form_title.configure(text="Book Edition")
            self.add_button.configure(text="Edit Book")
            self.available_checkbox.deselect()
            self.available_checkbox.configure(state="disabled")  
            self.current_mode = "edition"
    
# =============================================================
# Edit Command
# =============================================================

    def edit(self, book: dict[str, Any]) -> None:
        if book is None:
            return
        self.current_book = book
        self.form_clear()
        self.current_mode = "edition"
        self.mode_change("edition")
        self.fill_entries(book)

# =============================================================
# Entry Clear
# =============================================================

    def form_clear(self) -> None:

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

    def fill_entries(self, book: dict[str, Any]) -> None:

        self.title_entry.insert(0,  book["title"])
        self.author_entry.insert(0, book["author"])
        self.pages_entry.insert(0,  str(book["pages"]))
        self.year_entry.insert(0,   str(book["year"]))

# =============================================================
# Get Book's Data from User
# =============================================================

    def book_data(self) -> dict[str, Any] | None:

        title  = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        pages  = check_integer(self.pages_entry.get(), "Pages")
        if pages is None:
            return None
        year = check_integer(self.year_entry.get(), "Year")
        if year is None:
            return None
        available = bool(self.available_checkbox.get())
        
        return {
            "book_id"  : None if self.current_book is None else self.current_book["book_id"],
            "title"    : title, 
            "author"   : author, 
            "pages"    : pages, 
            "year"     : year, 
            "available": available if self.current_book is None else True, 
            "borrower" : None if self.current_book is None else self.current_book["borrower"]}