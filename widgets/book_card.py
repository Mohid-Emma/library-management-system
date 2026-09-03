#book_card.py

import customtkinter as     ctk
from   config        import theme

class BookCard(ctk.CTkFrame):
    def __init__(self, master, book, on_edit, on_delete, on_return, on_borrow):
        super().__init__(
            master        = master,
            corner_radius = 12,
            border_width  = 1,
            fg_color      = theme.surface,
            border_color  = theme.border)
        
        self.book      = book
        self.on_edit   = on_edit
        self.on_delete = on_delete
        self.on_return = on_return
        self.on_borrow = on_borrow

    
        self.create_layout()
        self.create_book_info()
        self.create_buttons()

# =============================================================
# Layout Creation
# =============================================================

    def create_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

# =============================================================
# Book Information
# =============================================================

    def create_book_info(self):
        info_frame = ctk.CTkFrame(
            master   = self,
            fg_color = theme.transparent)
        info_frame.grid(row=0, column=0, padx=15, pady=15, sticky="news")

        info_frame.grid_columnconfigure(0, weight=1)
    
    # =============================================================
    # Book Title and Author 
    # =============================================================

        # Title
        ctk.CTkLabel(
            master     = info_frame,
            text       = f"📖  {self.book.title}", 
            font       = ("Segoe UI", 16, "bold"),
            text_color = theme.text,
            anchor     = "w"
        ).grid(row=0, column=0, sticky="ew", pady=(0,5))

        # Author
        ctk.CTkLabel(
            master     = info_frame,
            text       = f"By {self.book.author}", 
            font       = ("Segoe UI", 12),
            text_color = theme.text_muted,
            anchor     = "w"
        ).grid(row=1, column=0, sticky="ew", pady=(0,12))

    # =============================================================
    # Details
    # =============================================================

        details_frame = ctk.CTkFrame(
            master   = info_frame,
            fg_color = theme.transparent)

        details_frame.grid(row=2, column=0, sticky="ew")

        self.create_detail(details_frame, "Pages", str(self.book.pages), 0)
        self.create_detail(details_frame, "Year" , str(self.book.year) , 1)

    # =============================================================
    # Status
    # =============================================================

        if self.book.available:
            status_text  = "● Available"
            status_color = theme.success
        else:
            status_text  = "● Borrowed"
            status_color = theme.warning

        # Status
        ctk.CTkLabel(
            master     = details_frame,
            text       = status_text, 
            font       = ("Segoe UI", 12, "bold"),
            text_color = status_color,
            anchor     = "w"
        ).grid(row=0, column=2, pady=(25,0), sticky="ew")

        if self.book.borrower:

        # Borrower

            ctk.CTkLabel(
            master     = info_frame,
            text       = f"Borrowed by {self.book.borrower}", 
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted,
            anchor     = "w"
        ).grid(row=3, column=0, pady=(8,0), sticky="w")

# =============================================================
# Details Creation
# =============================================================

    def create_detail(self, parent, label, value, column):

        frame = ctk.CTkFrame(
            master   = parent,
            fg_color = theme.transparent)
        
        frame.grid(row=0, column=column, padx=(0,25), sticky="w")
        
        ctk.CTkLabel(
            master     = frame,
            text       = label, 
            font       = ("Segoe UI", 10),
            text_color = theme.text_muted,
            anchor     = "w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            master     = frame,
            text       = value, 
            font       = ("Segoe UI", 12, "bold"),
            text_color = theme.text,
            anchor     = "w"
        ).pack(anchor="w")

# =============================================================
# Button Creation
# =============================================================

    def create_buttons(self):

        button_frame = ctk.CTkFrame(
            master   = self, 
            fg_color = theme.transparent)
        button_frame.grid(row=0, column=1, padx=15, pady=15, sticky="e") 

    # =============================================================
    # Edit Button
    # =============================================================

        self.edit_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Edit",
            width         = 90,
            height        = 35,
            corner_radius = 8, 
            fg_color      = theme.accent,
            hover_color   = theme.accent_hover,
            font          = ("Segoe UI", 11, "bold"),
            command       = lambda: self.on_edit(self.book))
        self.edit_button.pack(pady=(0,7))

    # =============================================================
    # Delete Button
    # =============================================================

        self.delete_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Delete",
            width         = 90,
            height        = 35,
            corner_radius = 8, 
            fg_color      = theme.danger,
            hover_color   = theme.danger_hover,
            font          = ("Segoe UI", 11, "bold"),
            command       = lambda: self.on_delete(self.book))
        self.delete_button.pack(pady=7)

    # =============================================================
    # Return Button
    # =============================================================

        self.return_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Return",
            width         = 90,
            height        = 35,
            corner_radius = 8, 
            fg_color      = theme.surface_light,
            hover_color   = theme.border,
            font          = ("Segoe UI", 11, "bold"),
            command       = lambda: self.on_return(self.book))
        self.return_button.pack(pady=7)

    # =============================================================
    # Borrow Button
    # =============================================================

        self.borrow_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Borrow",
            width         = 90,
            height        = 35,
            corner_radius = 8, 
            fg_color      = theme.success,
            hover_color   = theme.success_hover,
            font          = ("Segoe UI", 11, "bold"),
            command       = lambda: self.on_borrow(self.book))
        self.borrow_button.pack(pady=(7,0))

    # =============================================================
    # Availablitily
    # =============================================================

        if self.book.available: 
            self.return_button.configure(
                state       = "disabled",
                fg_color    = theme.surface_light,
                hover_color = theme.border) 
            self.borrow_button.configure(
                fg_color    = theme.success,
                hover_color = theme.success_hover,
            )
        else:
            self.borrow_button.configure(
                state       = "disabled",
                fg_color    = theme.surface_light,
                hover_color = theme.border) 
            self.return_button.configure(
                fg_color    = theme.success,
                hover_color = theme.success_hover,
            )
