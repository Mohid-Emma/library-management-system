#book_list.py

import customtkinter as     ctk
from   config        import theme
from   widgets       import BookCard

class BookList(ctk.CTkScrollableFrame):
    def __init__(self, master):
            super().__init__(
            master                       = master, 
            corner_radius                = 10,
            fg_color                     = theme.background,
            scrollbar_button_color       = theme.surface_light,
            scrollbar_button_hover_color = theme.border)

            self.on_edit   = None
            self.on_delete = None
            self.on_return = None
            self.on_borrow = None
            
            self.create_layout()

# =============================================================
# Assignation Function to Variable
# =============================================================

    def set_callbacks(self, on_edit, on_delete, on_return, on_borrow):
        self.on_edit   = on_edit
        self.on_delete = on_delete
        self.on_return = on_return
        self.on_borrow = on_borrow

# ============================================================= 
# Layout Creation  
# ============================================================= 

    def create_layout(self): 
        self.grid_columnconfigure(0, weight=1)

# =============================================================
# Book Display
# =============================================================

    def display_books(self, books):

        self.clear()

        if not books:
            self.show_empty_message()
            return

        for book in books:
            BookCard(
                master    = self,
                book      = book, 
                on_edit   = self.on_edit, 
                on_delete = self.on_delete, 
                on_return = self.on_return, 
                on_borrow = self.on_borrow 
                ).grid(row=self.winfo_children().__len__(), column=0, padx=10, pady=8, sticky="ew")

# =============================================================
# Destroy of Book Display
# =============================================================

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

# =============================================================
# Display When Library is Empty
# =============================================================

    def show_empty_message(self):
        empty_frame = ctk.CTkFrame(
            master   = self, 
            fg_color = theme.transparent)
        empty_frame.grid(row=0, column=0, padx=20, pady=60, sticky="news")

        ctk.CTkLabel( 
            master = empty_frame, 
            text   = "📚", 
            font   = ("Segoe UI Emoji", 40)
            ).pack( pady=(0, 10))

        ctk.CTkLabel(
            master     = empty_frame, 
            text       = "No books available.",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text
            ).pack(pady=5)

        ctk.CTkLabel(
            master     = empty_frame, 
            text       = "Try adding a book or changing your search.",
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted
            ).pack(pady=5) 