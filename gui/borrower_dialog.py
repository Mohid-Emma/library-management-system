#borrower_dialog.py

import customtkinter as ctk
from tkinter import messagebox
from models.borrower import Borrower


class BorrowerDialog(ctk.CTkToplevel):
    def __init__(self, parent, book):
        super().__init__(parent)

        self.grab_set()
        self.resizable(False, False)
        self.parent = parent
        self.book = book

        self.title("Borrow")
        self.geometry("500x300")
        self.minsize(300, 200)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.create_window()
        self.create_widget()


    def create_window(self):
        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True)

    def create_widget(self):
        self.book_label = ctk.CTkLabel(self.main, text = f"Title: {self.book.title}", font=("Arial", 27, "bold"))
        self.book_label.pack(pady=10)

        self.borrower_name_entry = ctk.CTkEntry(self.main, placeholder_text="What is your name?", width=300)
        self.borrower_name_entry.pack(pady=10)

        button_frame = ctk.CTkFrame(self.main)
        button_frame.pack(anchor="c", padx=10, pady=10)

        ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_borrow).pack(side="left",padx=5, pady=5)
        ctk.CTkButton(button_frame, text="Borrow", command=self.borrow_book).pack(side="left",padx=5, pady=5)

    def borrow_book(self):
        name = self.borrower_name_entry.get().strip()
        try:
            borrow = Borrower(name)
        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return
        if self.book.borrow(borrow):
            self.parent.refresh()
            self.parent.set_status(f"📕 Borrowed '{self.book.title}'.")
        else:
            self.parent.set_status(f"{self.book.title} is already borrowed.")
        self.destroy()

    def cancel_borrow(self):
        self.destroy()

