#book_list.py

import customtkinter as     ctk
from   widgets       import BookCard

class BookList(ctk.CTkScrollableFrame):
    def __init__(self, master):
            super().__init__(master, label_text="Books in Library", label_font=("Helvetica", 24, "bold"), corner_radius= 20, label_anchor="center")

    def set_callbacks(self, on_edit, on_delete, on_return, on_borrow):
        self.on_edit   = on_edit
        self.on_delete = on_delete
        self.on_return = on_return
        self.on_borrow = on_borrow

    def display_books(self, books):
        self.clear()
        if not books:
            self.show_empty_message()
            return
        for book in books:
            BookCard(
                self,
                book, 
                self.on_edit, 
                self.on_delete, 
                self.on_return, 
                self.on_borrow 
                ).pack(padx=20, pady=20, expand="True", fill="both")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_empty_message(self):
        ctk.CTkLabel(self, text="No books available.").pack(pady=20)