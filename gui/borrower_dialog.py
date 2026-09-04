#borrower_dialog.py

import customtkinter as     ctk
from   config        import theme

class BorrowerDialog(ctk.CTkToplevel):
    def __init__(self, master, book_title) -> None:
        super().__init__(master)

        self.result     = None 

    # =============================================================
    # Window Configuration
    # =============================================================

        self.title("Borrow Book")
        self.geometry("500x360")
        self.resizable(False, False)

        self.configure(fg_color=theme.background)
        self.transient(master)
        self.grab_set()

        self.create_widgets(book_title)

# =============================================================
# GUI/UI
# =============================================================

    def create_widgets(self, book_title : str) -> None:

        self.grid_columnconfigure(0, weight=1)

    # =============================================================
    # Main Card
    # =============================================================

        self.card = ctk.CTkFrame(
            master        = self,
            corner_radius = 15,
            border_width  = 1,
            border_color  = theme.border,
            fg_color      = theme.surface)
        self.card.grid(row=0, column=0, padx=25, pady=25, sticky="news")

        self.card.grid_columnconfigure(0, weight=1)
    
    # =============================================================
    # Title
    # =============================================================
        
        ctk.CTkLabel(
            master     = self.card,
            text       = "📖 Borrow Book",
            font       = ("Segoe UI", 21, "bold"),
            text_color = theme.text
        ).grid(row=0, column=0, padx=25, pady=(25,5), sticky="w")

    # =============================================================
    # Book
    # =============================================================
        
        ctk.CTkLabel(
            master     = self.card,
            text       = book_title,
            font       = ("Segoe UI", 12),
            text_color = theme.text_muted,
            wraplength = 330,
            justify    = "left"
        ).grid(row=1, column=0, padx=25, pady=(0,20), sticky="w")

        ctk.CTkLabel(
            master     = self.card,
            text       = "Borrower Name",
            font       = ("Segoe UI", 12, "bold"),
            text_color = theme.text,
        ).grid(row=2, column=0, padx=25, pady=(0,5), sticky="w")

        self.name_entry = ctk.CTkEntry(
            master                 = self.card, 
            placeholder_text       = "Enter Borrower Name",
            height                 = 40,
            corner_radius          = 9,
            border_width           = 1,
            border_color           = theme.border,
            fg_color               = theme.background,
            text_color             = theme.text,
            placeholder_text_color = theme.text_muted,
            font                   = ("Segoe UI", 13))
        self.name_entry.grid(row=3, column=0, padx=25, pady=(0,20), sticky="ew")


    # =============================================================
    # Button Creation
    # =============================================================

        button_frame = ctk.CTkFrame(
            master   = self.card,
            fg_color = theme.transparent)
        button_frame.grid(row=4, column=0, padx=25, pady=(0,25), sticky="ew")

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.cancel_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Cancel",
            height        = 40,
            corner_radius = 9, 
            fg_color      = theme.surface_light,
            hover_color   = theme.border,
            text_color    = theme.text,
            font          = ("Segoe UI", 12, "bold"),
            command       = self.cancel)
        self.cancel_button.grid(row=0, column=0, padx=(0,5), sticky="ew")

        self.borrow_button = ctk.CTkButton(
            master        = button_frame, 
            text          = "Borrow Book",
            height        = 40,
            corner_radius = 9, 
            fg_color      = theme.success,
            hover_color   = theme.success_hover,
            font          = ("Segoe UI", 12, "bold"),
            command       = self.confirm)
        self.borrow_button.grid(row=0, column=1, padx=(5,0), sticky="ew")

        self.name_entry.focus_set()

        self.bind("<Return>", lambda event: self.confirm())
        self.bind("<Escape>", lambda event: self.cancel())

# ============================================================= 
# Confirm 
# =============================================================

    def confirm(self) -> None:
        name = self.name_entry.get().strip()
        if not name:
            self.name_entry.configure(border_name = theme.warning)
            self.name_entry.focus_set()
            return
        self.result = name
        self.destroy()

# =============================================================
# Cancel 
# =============================================================

    def cancel(self) -> None:
        self.result = None
        self.destroy()


# =============================================================
# Result
# =============================================================

    def get_result(self) -> str:
        return self.result
