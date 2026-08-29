#borrower_dialog.py

import customtkinter as     ctk
from   tkinter       import messagebox
from   models        import Borrower

class BorrowerDialog(ctk.CTkToplevel):
    def __init__(self, parent, book):
        super().__init__(parent)
        self.parent     = parent
        self.book_title = book
        self.result     = None 

    # =============================================================
    # Window Configuration
    # =============================================================

        self.grab_set()
        self.resizable(False, False)

        self.title("Borrow")
        self.geometry("500x300")
        self.minsize(300, 200)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.create_window()
        self.create_label()
        self.create_entry()
        self.create_button()

    # =============================================================
    # Frame Configuration
    # =============================================================

    def create_window(self):
        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True)

    # =============================================================
    # Label Creation
    # =============================================================

    def create_label(self):
        self.book_label = ctk.CTkLabel(self.main, text = f"Title: {self.book_title}", font=("Segoe UI", 27, "bold"))
        self.book_label.pack(pady=20)

    # =============================================================
    # Entry Creation
    # =============================================================

    def create_entry(self):

        self.borrower_name_entry = ctk.CTkEntry(self.main, placeholder_text="What is your name?", width=400, height= 30)
        self.borrower_name_entry.pack(pady=10)

    # =============================================================
    # Button Creation
    # =============================================================

    def create_button(self):
    
        button_frame = ctk.CTkFrame(self.main)
        button_frame.pack(anchor="c", padx=10, pady=10)

        button_frame.rowconfigure(0, weight=0, uniform="a")
        button_frame.columnconfigure((0,1), weight=1, uniform="a")

        ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_borrow).grid(row = 0, column = 0, sticky="news", padx=10, pady=5)
        ctk.CTkButton(button_frame, text="Borrow", command=self.borrow_book  ).grid(row = 0, column = 1, sticky="news", padx=10, pady=5)

    # =============================================================
    # Borrower Name
    # =============================================================

    def borrow_book(self):
        name = self.borrower_name_entry.get().strip()
        try:
            self.result = Borrower(name)
        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error)+" "*20)
            return 
        self.destroy()

    # =============================================================
    # Get Result From This Windows
    # =============================================================

    def get_result(self):
        return self.result

    # =============================================================
    # Close Window
    # =============================================================

    def cancel_borrow(self):
        self.destroy()

