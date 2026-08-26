#app.py

import customtkinter as     ctk
from   library       import Library
from  .controller    import Controller
from   widgets       import BookForm, ToolBar, BookList, StatusBar


class LibraryApp(ctk.CTk):
    def __init__(self, db):
        super().__init__()

    # =============================================================
    # Window Configuration
    # =============================================================

        self.title("Library Management System")
        self.geometry("1200x800")
        self.minsize(500, 700)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.create_window()

    # =============================================================
    # Modules Initialization and Configuration
    # =============================================================
        self.library = Library(db)

        self.book_form = BookForm(self.left_frame)
        self.book_form.place(x=0, y=0, relwidth=1, relheight= 0.6)

        self.create_book_button()

        self.tool_bar = ToolBar(self.right_frame)
        self.tool_bar.place(x=0, y=0, relwidth=1, relheight= 0.1) 

        self.book_list = BookList(self.right_frame)
        self.book_list.place(x=0, rely=0.1, relwidth=1, relheight= 0.8) 

        self.status_bar = StatusBar(self.footer_frame)
        self.status_bar.grid(sticky="nsew")

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

    # =============================================================
    # ?????????????????
    # =============================================================

        self.assign_button_command()
        self.controller.refresh_books()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # =============================================================
    # Frame Configuration
    # =============================================================

    def create_window(self):

        self.header_frame = ctk.CTkFrame(self)
        self.left_frame   = ctk.CTkFrame(self)
        self.right_frame  = ctk.CTkFrame(self)
        self.footer_frame = ctk.CTkFrame(self, height=40)

        self.header_frame.place(    x= 0,      y= 0,    relwidth= 1,   relheight= 0.1)
        self.left_frame.place(      x= 0,   rely= 0.1,  relwidth= 0.4, relheight= 0.9)
        self.right_frame.place(  relx= 0.4, rely= 0.1,  relwidth= 0.6, relheight= 0.9)
        self.footer_frame.place(    x= 0,   rely= 0.95, relwidth= 1,   relheight= 0.1)


        self.title_label  = ctk.CTkLabel(self.header_frame, text ="📚 Library Management System", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=15, expand= True, fill="both")

    # =============================================================
    # Button Creation
    # =============================================================

    def create_book_button(self):
        button_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        button_frame.place(x=0, rely=0.6, relwidth=1, relheight= 0.1)

        self.cancel_button = ctk.CTkButton(button_frame, text="Cancel",   corner_radius=20, font=("Helvetica", 15))
        self.add_button    = ctk.CTkButton(button_frame, text="Add Book", corner_radius=20, font=("Helvetica", 15)) 

        button_frame.rowconfigure(0, weight=1, uniform="a")
        button_frame.columnconfigure((0,1), weight=1, uniform="a")

    def assign_button_command(self):
        self.add_button.configure(command=self.controller.add_book)
        
        self.add_button.grid(row= 0, column = 0, columnspan= 2, sticky="news", padx=20, pady=10)

        self.cancel_button.configure(command=self.controller.cancel_edit)

    # =============================================================
    # Edit Mode GUI
    # =============================================================

    def set_edit_mode(self, mode):
        if mode:
            self.add_button.grid(   row= 0, column = 1, sticky="news", padx=20, pady=15)
            self.cancel_button.grid(row= 0, column = 0, sticky="news", padx=20, pady=15)
            self.add_button.configure( text = "Save Changes")
            self.title_label.configure(text = "🟡 Editing Book")

        else:
            self.cancel_button.grid_forget()
            self.add_button.grid(row= 0, column = 0, columnspan= 2, sticky="news", padx=20, pady=10)
            self.add_button.configure( text = "Add Book")
            self.title_label.configure(text = "Library Management System")
            self.title("Library Management System")

    # =============================================================
    # System Close 
    # =============================================================

    def on_close(self):
        self.library.db.close()
        self.destroy()