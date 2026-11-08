# app.py
import customtkinter as ctk
from utils  import app_id, icon_extract
from typing import Any
from config import theme


class MainWindows(ctk.CTk):
    def __init__(self, ui_compounds: dict[str, Any], operation) -> None:
        super().__init__(fg_color= theme.background)

    # =============================================================
    # Window Configuration
    # =============================================================

        self.title("Library Management System")
        self.geometry("1200x800")
        self.minsize(900, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.library = None # Library(db)
        self.ui_compounds = ui_compounds
        self.form_operation = operation["add"]
        self.toolbar_operation = operation["toolbar"]
        self.card_operation = operation["card"]
        

        app_id()
        icon_extract(self)

        self.create_layout()
        self.create_frame()

        self.create_header()
        self.create_sidebar()
        self.create_main_content()
        self.create_footer()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

# =============================================================
# Layout Creation
# =============================================================

    def create_layout(self) -> None:

        # Main window rows
        self.grid_rowconfigure(0, weight=0)   # Header
        self.grid_rowconfigure(1, weight=1)   # Content
        self.grid_rowconfigure(2, weight=0)   # Footer

        # Main window columns
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Main Content

# =============================================================
# Frame Creation
# =============================================================

    def create_frame(self) -> None:

    # Header Frame
        self.header_frame = ctk.CTkFrame(
            master        = self, 
            height        = 75, 
            corner_radius = 0, 
            fg_color      = theme.surface)
        
        self.header_frame.grid(row=0,  column=0, columnspan=2, sticky="news")
        self.header_frame.grid_propagate(False)

    # SideBar Frame
        self.sidebar_frame = ctk.CTkFrame(
            master        = self, 
            width         = 230, 
            corner_radius = 0, 
            fg_color      = theme.sidebar)
        self.sidebar_frame.grid(row=1, column=0, sticky="news")
        self.sidebar_frame.grid_propagate(False)

    # Main Frame
        self.main_frame = ctk.CTkFrame(
            master        = self, 
            corner_radius = 0, 
            fg_color      = theme.background)
        self.main_frame.grid(row=1, column=1, padx=15, pady=15, sticky="news")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=3)

    # Footer Frame
        self.footer_frame = ctk.CTkFrame(
            master        = self, 
            height        = 40, 
            corner_radius = 0, 
            fg_color      = theme.surface)
        self.footer_frame.grid(row=2,  column=0, columnspan=2, sticky="news")
        self.footer_frame.grid_propagate(False)

# =============================================================
# Header Creation
# =============================================================
    
    def create_header(self) -> None:

        self.header_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            master     = self.header_frame, 
            text       = "📚 Library Management System", 
            font       = ("Segoe UI", 24, "bold"), 
            text_color = theme.text)
        
        self.title_label.grid(row=0, column=0, padx=25, pady=10, sticky="w")

        self.header_status = ctk.CTkLabel(
            master     = self.header_frame, 
            text       = "Library Manager", 
            font       = ("Segoe UI", 12), 
            text_color = theme.text_muted)
        
        self.header_status.grid(row=0, column=1, padx=25, sticky="e")

# =============================================================
#  SideBar Creation
# =============================================================

    def create_sidebar(self) -> None:
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

    # Logo
        logo_frame = ctk.CTkFrame(self.sidebar_frame, fg_color = theme.transparent)
        logo_frame.grid(row=0, column=0, padx=20, pady=(25,30), sticky="ew")
        logo_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            master = logo_frame, 
            text   = "📖", 
            font   = ("Segoe UI Emoji", 30)
        ).grid(row=0, column=0)
        
        ctk.CTkLabel(
            master     = logo_frame, 
            text       = "LIBRARY", 
            font       = ("Segoe UI", 17, "bold"), 
            text_color = theme.text
        ).grid(row=0, column=1, padx=10, sticky="w")

    # Navigation Frame
        ctk.CTkLabel(
            master     = self.sidebar_frame,
            text       = "NAVIGATION",
            font       = ("Segoe UI", 10, "bold"),
            text_color = theme.text_muted
        ).grid(row=1, column=0, padx=20, pady=(0,10), sticky="w")

    # Book Button
        self.books_button = ctk.CTkButton(
            master        = self.sidebar_frame,
            text          = "📚   Books",
            anchor        = "w",
            height        = 45,
            corner_radius = 10,
            fg_color      = theme.accent,
            text_color    = theme.text,
            hover_color   = theme.accent_hover,
            font          = ("Segoe UI", 10, "bold"),
            command       = self.show_books )

        self.books_button.grid(row=2, column=0, padx=12, pady=4, sticky="ew")

    # Book Addition Button
        self.add_book_button = ctk.CTkButton(
            master        = self.sidebar_frame,
            text          = "➕   Add Book",
            anchor        = "w",
            height        = 45,
            corner_radius = 10,
            fg_color      = theme.transparent,
            text_color    = theme.text,
            hover_color   = theme.surface,
            font          = ("Segoe UI", 13),
            command       = self.show_add_books )

        self.add_book_button.grid(row=3, column=0, padx=12, pady=4, sticky="ew")

    # Information Card
        info_card = ctk.CTkFrame(
            master        = self.sidebar_frame, 
            corner_radius = 12,
            fg_color      = theme.surface)
        info_card.grid(row=5, column=0, padx=15, pady=20, sticky="ew")

        ctk.CTkLabel(
            master     = info_card,
            text       = "Library",
            font       = ("Segoe UI", 13, "bold"),
            text_color = theme.text
        ).pack(anchor="w", padx=15, pady=(15,3))

        ctk.CTkLabel(
            master     = info_card,
            text       = "Manage your books\nand library collection.",
            justify    = "left",
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted
        ).pack(anchor="w", padx=15, pady=(0,15))    

# =============================================================
#  Main Content
# =============================================================
    def create_main_content(self):
    # Book Form
        self.book_form = self.ui_compounds["form"](self.main_frame, self.form_operation)
        self.book_form.grid(row=0, column=0, padx=10, pady=5, sticky="news")

    # Book Panel
        self.book_view = self.ui_compounds["view"](self.main_frame, self.ui_compounds["card"], self.toolbar_operation, self.card_operation)
        self.book_view.grid(row=0, column=1, padx=20, pady=5, sticky="news")

# =============================================================
#  Creation Footer
# =============================================================
    
    def create_footer(self) -> None:
        self.status_bar = self.ui_compounds["status"](self.footer_frame)
        self.status_bar.pack(fill="both", expand=True, padx=15)

# =============================================================
# Assign Button Cammand
# =============================================================

    def assign_button_command(self) -> None:
        self.add_button.configure(command=self.controller.add_book)
        self.cancel_button.configure(command=self.controller.cancel_edit)    



# =============================================================
#  Creation
# =============================================================

    def show_books(self) -> None:
        self.books_button.configure(fg_color = theme.accent)
        self.add_book_button.configure(fg_color = theme.transparent)

    def show_add_books(self) -> None:
        self.add_book_button.configure(fg_color = theme.surface)
        self.books_button.configure(fg_color = theme.transparent)

        self.book_form.title_entry.focus_set()
        
# =============================================================
# Edit Mode GUI
# =============================================================

    def set_edit_mode(self, mode : bool) -> None:

        if mode:            
            self.form_title.configure(    text = "Edit Book")
            self.title_label.configure(   text = "🟡  Editing Book")
            self.header_status.configure( text = "Editing")
            self.title("Editing Book - Library Management System")

            self.cancel_button.grid(row= 0, column = 0, padx=(0,5), sticky="ew")
            self.add_button.grid(   row= 0, column = 1, padx=(5,0), sticky="ew")

            self.add_button.configure(text = "Save Changes")

        else:
            self.cancel_button.grid_forget()
            self.add_button.grid(row= 0, column = 0, columnspan= 2, padx=0, sticky="ew")
            self.add_button.configure(    text = "Add Book")
            self.form_title.configure(    text = "Add New Book")
            self.title_label.configure(   text = "📚  Library Management System")
            self.header_status.configure( text = "Library Manager")
            self.title("Library Management System")

# =============================================================
# System Close 
# =============================================================

    def on_close(self) -> None:
        # self.library.db.close()
        self.destroy()

# =============================================================
    
    def book_data(self) -> dict[str: Any] | None:
        return self.book_form.book_data() if self.book_form.book_data is not None else None

    def form_clear(self) -> None:
        self.book_form.form_clear()

    def set_status(self, message: str) -> None:
        self.status_bar.set_status(message)

    def display_books(self, books: list[dict[str: Any]]) -> None:
        self.book_view.display_books(books)

    def edit(self, book: dict[str, Any]) -> None:
        self.book_form.edit(book)
    
    def cancel_edit(self) -> None:
        self.book_form.cancel()
    
    def dialog(self, title: str) -> str:
        dialog = self.ui_compounds["dialog"](self, title)
        self.wait_window(dialog)
        return dialog.get_result()