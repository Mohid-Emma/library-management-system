#app.py
import tkinter       as     tk
import customtkinter as     ctk
from   config        import theme
from   library       import Library
from  .controller    import Controller
from   utils         import app_id, icon_extract
from   widgets       import BookForm, ToolBar, BookList, StatusBar


class LibraryApp(ctk.CTk):
    def __init__(self, db):
        super().__init__()

    # =============================================================
    # Window Configuration
    # =============================================================

        self.title("Library Management System")
        self.geometry("1200x800")
        self.minsize(900, 650)

        app_id()
        icon_extract(self)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color= theme.background)

        # =============================================================
        # Data
        # =============================================================

        self.library = Library(db)

        # =============================================================
        # GUI Creation
        # =============================================================

        self.create_layout()
        self.create_frame()
        self.create_header()
        self.create_sidebar()
        self.create_form_panel()
        self.create_books_panel()
        self.create_footer()

    # =============================================================
    # Modules Assignation
    # =============================================================

        self.controller = Controller(
            app       = self, 
            library   = self.library, 
            book_form = self.book_form, 
            book_list = self.book_list, 
            toolbar   = self.tool_bar, 
            statusbar = self.status_bar )

        self.tool_bar.set_callbacks(
            on_search = self.controller.search_books, 
            on_sort   = self.controller.sort_books )
        
        self.book_list.set_callbacks(
            on_edit   = self.controller.edit_book, 
            on_delete = self.controller.delete_book, 
            on_return = self.controller.return_book, 
            on_borrow = self.controller.borrow_book )

        self.controller.set_callback(
            on_set_edit_mode = self.set_edit_mode )

        self.assign_button_command()
        self.controller.refresh_books()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

# =============================================================
# Layout Creation
# =============================================================

    def create_layout(self):

        # Main window rows
        self.grid_rowconfigure(0, weight=0)   # Header
        self.grid_rowconfigure(1, weight=1)   # Content
        self.grid_rowconfigure(2, weight=0)   # Footer

        # Main window columns
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Main content

# =============================================================
# Frame Creation
# =============================================================

    def create_frame(self):

    # =============================================================
    # Header Frame
    # =============================================================
    
        self.header_frame = ctk.CTkFrame(
            master        = self, 
            height        = 75, 
            corner_radius = 0, 
            fg_color      = theme.surface)
        
        self.header_frame.grid(row=0,  column=0, columnspan=2, sticky="news")
        self.header_frame.grid_propagate(False)

    # =============================================================
    # SideBar Frame
    # =============================================================
    
        self.sidebar_frame = ctk.CTkFrame(
            master        = self, 
            width         = 230, 
            corner_radius = 0, 
            fg_color      = theme.sidebar)
        self.sidebar_frame.grid(row=1, column=0, sticky="news")
        self.sidebar_frame.grid_propagate(False)

    # =============================================================
    # Main Frame
    # =============================================================
    
        self.main_frame = ctk.CTkFrame(
            master        = self, 
            corner_radius = 0, 
            fg_color      = theme.background)
        self.main_frame.grid(row=1, column=1, padx=15, pady=15, sticky="news")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=3)

    # =============================================================
    # Footer Frame
    # =============================================================
    
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
    
    def create_header(self):

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
#  Creation SideBar
# =============================================================

    def create_sidebar(self):
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

    # =========================================================
    # Logo
    # =========================================================

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

    # =========================================================
    # Navigation Frame
    # =========================================================

        ctk.CTkLabel(
            master     = self.sidebar_frame,
            text       = "NAVIGATION",
            font       = ("Segoe UI", 10, "bold"),
            text_color = theme.text_muted
        ).grid(row=1, column=0, padx=20, pady=(0,10), sticky="w")

    # =========================================================
    # Book Button
    # =========================================================

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

    # =========================================================
    # Book Addition Button
    # =========================================================

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

    # =========================================================
    # Information Card
    # =========================================================

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
#  Creation Form Panel
# =============================================================
    
    def create_form_panel(self):
        
    # =========================================================
    # Form Panel Creation
    # =========================================================

        self.form_card = ctk.CTkFrame(
            master        = self.main_frame,
            corner_radius = 15,
            border_width  = 1,
            fg_color      = theme.surface,
            border_color  = theme.border)

        self.form_card.grid(row=0, column=0, sticky="news")
        self.form_card.grid_rowconfigure(1, weight=1)
        self.form_card.grid_columnconfigure(0, weight=1)

    # =========================================================
    # Form Panel Title
    # =========================================================

        self.form_title = ctk.CTkLabel(
            master     = self.form_card,
            text       = "Book Addition",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text)
        
        self.form_title.grid(row=0, column=0, padx=20, pady=(20,10), sticky="w")

    # =========================================================
    # Book Form
    # =========================================================

        self.book_form = BookForm(self.form_card)
        self.book_form.grid(row=1, column=0, padx=20, pady=5, sticky="news")

    # =============================================================
    # Button Creation
    # =============================================================

        self.button_frame = ctk.CTkFrame(
            master   = self.form_card,
            fg_color = theme.transparent)

        self.button_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)

        # Cancel
        self.cancel_button = ctk.CTkButton(
            master        = self.button_frame, 
            text          = "Cancel",   
            height        = 42,
            corner_radius = 10,
            fg_color      = theme.surface_light,
            hover_color   = theme.border, 
            font          = ("Segoe UI", 13, "bold"))

        # Addition
        self.add_button = ctk.CTkButton(
            master        = self.button_frame, 
            text          = "Add Book", 
            height        = 42,
            corner_radius = 10,
            fg_color      = theme.accent,
            hover_color   = theme.accent_hover, 
            font          = ("Segoe UI", 13, "bold"))

        self.add_button.grid(row=0, column=0, columnspan=2, sticky="ew")
                
# =============================================================
#  Creation Book Panel
# =============================================================
    
    def create_books_panel(self):

        self.books_card = ctk.CTkFrame(
            master        = self.main_frame,
            corner_radius = 15,
            border_width  = 1,
            border_color  = theme.border,
            fg_color      = theme.surface)
        
        self.books_card.grid(row=0, column=1, padx=(15,0), sticky="news")

        self.books_card.grid_rowconfigure(2, weight=1)
        self.books_card.grid_columnconfigure(0, weight=1)
      
    # =============================================================
    #  Book Panel Title
    # =============================================================

        title_frame = ctk.CTkFrame(
            master   = self.books_card, 
            fg_color = theme.transparent)
          
        title_frame.grid(row=0, column=0, padx=15, pady=(15,5), sticky="ew")

        ctk.CTkLabel(
            master     = title_frame,
            text       = "Books",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text 
        ).pack(anchor="w")

        ctk.CTkLabel(
            master     = title_frame,
            text       = "Browse and manage your collection",
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted
        ).pack(anchor="w")

    # =============================================================
    #  Book Panel Widget
    # =============================================================

        # ToolBar
        self.tool_bar = ToolBar(self.books_card)
        self.tool_bar.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        # BookList
        self.book_list = BookList(self.books_card)
        self.book_list.grid(row=2, column=0, padx=15, pady=(0,15), sticky="news")
        
               
# =============================================================
#  Creation Footer
# =============================================================
    
    def create_footer(self):
        self.status_bar = StatusBar(self.footer_frame)
        self.status_bar.pack(fill="both", expand=True, padx=15)

# =============================================================
# Assign Button Cammand
# =============================================================
    def assign_button_command(self):
        self.add_button.configure(command=self.controller.add_book)
        self.cancel_button.configure(command=self.controller.cancel_edit)    

# =============================================================
#  Creation
# =============================================================

    def show_books(self):
        self.books_button.configure(fg_color = theme.accent)
        self.add_book_button.configure(fg_color = theme.transparent)

    def show_add_books(self):
        self.add_book_button.configure(fg_color = theme.surface)
        self.books_button.configure(fg_color = theme.transparent)

        self.book_form.title_entry.focus_set()
        
# =============================================================
# Edit Mode GUI
# =============================================================

    def set_edit_mode(self, mode):
        if mode:
            
            self.form_title.configure(    text = "Edit Book")
            self.title_label.configure(   text = "🟡  Editing Book")
            self.header_status.configure( text = "Editing")
            self.title("Editing Book - Library Management System")

            self.cancel_button.grid(row= 0, column = 0, padx=(0,5), sticky="ew")
            self.add_button.grid(row= 0, column = 1, padx=(5,0), sticky="ew")

            self.add_button.configure(text  = "Save Changes")


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

    def on_close(self):
        self.library.db.close()
        self.destroy()