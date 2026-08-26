#book_card.py

import customtkinter as ctk

class BookCard(ctk.CTkFrame):
    def __init__(self, master, book, on_edit, on_delete, on_return, on_borrow):
        super().__init__(master)
        self.book      = book
        self.on_edit   = on_edit
        self.on_delete = on_delete
        self.on_return = on_return
        self.on_borrow = on_borrow

        self.create_widgets()

    # =============================================================
    # Widget Creation
    # =============================================================

    def create_widgets(self):
        
        self.create_label(f"Title : {self.book.title}" , font=("Helvetica", 20, "bold"))
        self.create_label(f"Author: {self.book.author}", font=("Helvetica", 15))
        self.create_label(f"Pages : {self.book.pages}" , font=("Helvetica", 15))
        self.create_label(f"Year  : {self.book.year}"  , font=("Helvetica", 15))

        if self.book.borrower:
            status = f"Borrowed by {self.book.borrower}"
        else:
            status = "Available"
        ctk.CTkLabel(self,text=f"Status: {status}", font=("Helvetica", 15)).pack(padx=5, pady=5, anchor="w")

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(padx=5, pady=5)

        button_frame.rowconfigure(0, weight=0, uniform="a")
        button_frame.columnconfigure((0,1,2,3), weight=1, uniform="a")

        self.create_button(button_frame, "Edit"  , lambda: self.on_edit(self.book)  , 0)
        self.create_button(button_frame, "Delete", lambda: self.on_delete(self.book), 1)
        return_btn = self.create_button(button_frame, "Return", lambda: self.on_return(self.book), 2)
        borrow_btn = self.create_button(button_frame, "Borrow", lambda: self.on_borrow(self.book), 3)

        if self.book.available: 
            return_btn.configure(state="disabled") 
        else:
            borrow_btn.configure(state="disabled") 

    # =============================================================
    # Label creation
    # =============================================================

    def create_label(self, text, **kwargs):
        ctk.CTkLabel(self, text= text, **kwargs).pack(padx=5, pady=5, anchor="w")

    # =============================================================
    # Button Creation
    # =============================================================

    def create_button(self, parent, text, command, column):
        button = ctk.CTkButton(parent, text=text, command=command, corner_radius=20, font=("Helvetica", 12))
        button.grid(row = 0, column = column, sticky="news", padx=10, pady=5)
        return button
    