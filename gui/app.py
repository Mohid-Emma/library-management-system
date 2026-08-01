#app.py
import customtkinter as ctk
from library.library import Library
from models.book import Book
from utils.helpers import check_integer
from tkinter import messagebox
from gui.borrower_dialog import BorrowerDialog


class LibraryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.library = Library()
        self.library.load()
        self.current_book = None

        self.title("Library Management System")
        self.geometry("1100x800")
        self.minsize(900, 600)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.create_window()
        self.create_input_widget()
        self.create_book_widget()

    def create_window(self):

        self.header = ctk.CTkFrame(self, height=70)
        self.header.pack(fill="x")

        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True)

        self.footer = ctk.CTkFrame(self, height=40)
        self.footer.pack(fill="x")

        self.title_label = ctk.CTkLabel(self.header, text ="📚 Library Management System", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=15)

    def create_entry(self, placeholder):

        entry = ctk.CTkEntry(self.main, placeholder_text=placeholder, width=300)
        entry.pack(pady=10)
        return entry

    def create_input_widget(self):

        self.title_entry  = self.create_entry("Book Title")
        self.author_entry = self.create_entry("Author")
        self.pages_entry  = self.create_entry("Pages")
        self.year_entry   = self.create_entry("Publication Year")

        self.available_checkbox = ctk.CTkCheckBox(self.main, text="Available")
        self.available_checkbox.pack(pady=10)


    def create_book_widget(self):

        button_frame = ctk.CTkFrame(self.main, fg_color="transparent")
        button_frame.pack(anchor="c", padx=10, pady=10)

        self.cancel_button = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel_edit)
        self.add_button = ctk.CTkButton(button_frame, text="Add Book", command=self.add_book)
        self.add_button.pack(side="left",padx=5, pady=5)

        self.books_label = ctk.CTkLabel(self.main, text="Books in Library", font=("Arial", 18, 'bold'))
        self.books_label.pack(pady=(20,5))

        self.create_search_widget()

        sorted_option = ["Title (A-Z)","Title (Z-A)","Author","Year (Newest)","Year (Oldest)","Pages (Smallest)","Pages (Largest)","Available","Borrowed"]
        self.sort_menu = ctk.CTkOptionMenu(self.main, values=sorted_option, command=self.sort_books)
        self.sort_menu.pack(pady=10)

        self.books_frame = ctk.CTkScrollableFrame(self.main)
        self.books_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.update_book_list()

        self.status_label = ctk.CTkLabel(self.footer, text="🟢 Ready", anchor="w")
        self.status_label.pack(fill="x", padx=10)

    def create_search_widget(self):

        self.search_entry = ctk.CTkEntry(self.main, placeholder_text="Search books...", width=200)
        self.search_entry.pack(pady=10)

        self.search_entry.bind("<KeyRelease>", self.search_book)


    def create_book_card(self, book):

        book_frame = ctk.CTkFrame(self.books_frame)
        book_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(book_frame,text=f"Title: {book.title}", font=("Arial", 16, 'bold')).pack(anchor="w", padx=10, pady=(10,2))
        ctk.CTkLabel(book_frame,text=f"Author: {book.author}").pack(anchor="w", padx=10)
        ctk.CTkLabel(book_frame,text=f"Pages : {book.pages}").pack(anchor="w", padx=10)
        ctk.CTkLabel(book_frame,text=f"Year  : {book.year}").pack(anchor="w", padx=10)

        available_lbl = ctk.CTkLabel(book_frame,text=f"Status: {'Available' if book.available else 'Borrowed'}")
        available_lbl.pack(anchor="w", padx=10, pady=(0,10))
        if book.borrower is not None:
            available_lbl.configure(text=f"Status: Borrowed by {book.borrower}")

        button_frame = ctk.CTkFrame(book_frame, fg_color="transparent")
        button_frame.pack(anchor="c", padx=10, pady=10)

        self.create_button(button_frame, "Edit", lambda b=book: self.edit_book(b))
        self.create_button(button_frame, "Delete", lambda b=book: self.delete_book(b))
        return_btn = self.create_button(button_frame, "Return", lambda b=book: self.return_book(b))
        borrow_btn = self.create_button(button_frame, "Borrow", lambda: BorrowerDialog(self, book))

        return_btn.configure(state="disabled") if book.available else borrow_btn.configure(state="disabled")   

    def create_button(self, parent, text, command):
        button = ctk.CTkButton(parent, text=text, command=command)
        button.pack(side="left",padx=5, pady=5)
        return button

    def add_book(self):
        if self.current_book is None:
            self.create_new_book()
        else:
            self.save_book_changes()

    def get_book(self):
        title     = self.title_entry.get()
        author    = self.author_entry.get()
        pages     = check_integer(self.pages_entry.get(), "Pages")
        year      = check_integer(self.year_entry.get(), "Year")
        available = bool(self.available_checkbox.get())

        if pages is None or year is None:
            return
        try:
            book = Book(title, author, pages, year, available)
        except ValueError as error:
            messagebox.showerror("Invalid Input" ,str(error))
            return
        return book

    def create_new_book(self):
        book = self.get_book()
        if book is None:
            return
        
        if not self.library.add_book(book):
            self.set_status("Book already exists.")
            return
        self.refresh()
        self.clear_entries()

    def save_book_changes(self):
        updated_book = self.get_book()
        if updated_book is None:
            return
        self.current_book.update(updated_book)
        self.refresh()
        self.reset_form()


    def search_book(self, _):
        self.update_book_list(self.search_entry.get().strip().lower())

    def matches_search(self, book, query):
        borrower = ""
        if book.borrower:
            borrower = book.borrower.name.lower()
        return any((query in book.title.lower(), query in book.author.lower(), \
        query in str(book.year), query in borrower , query in ("available" if book.available else "borrowed")))

    def update_book_list(self, query=""):
        for widget in self.books_frame.winfo_children():
            widget.destroy()

        if not self.library.books:
            ctk.CTkLabel(self.books_frame, text="No books available").pack(pady=20)
            return

        found = False

        for book in self.library.books:
            if self.matches_search(book, query):
                self.create_book_card(book)
                found = True

        if not found:
            ctk.CTkLabel(self.books_frame, text="No matching books found.").pack(pady=20)

    def sort_books(self, choice):

        sort_options = {"Title (A-Z)": lambda b: b.title.lower(),
                    "Title (Z-A)": lambda b: b.title.lower(),
                    "Author": lambda b: b.author.lower(),
                    "Year (Newest)": lambda b: b.year,
                    "Year (Oldest)": lambda b: b.year,
                    "Pages (Smallest)": lambda b: b.pages,
                    "Pages (Largest)": lambda b: b.pages,
                    "Available": lambda b: (not b.available, b.title.lower()),
                    "Borrowed": lambda b: (b.available, b.title.lower())}

        key = sort_options.get(choice)
        if key is None:
            return
        self.library.books.sort(key=key, reverse=choice in ("Title (Z-A)", "Year (Newest)","Pages (Largest)"))

    def edit_book(self, book):
        self.current_book = book
        self.clear_entries()
        self.fill_entries(book)
        self.title(f"Editing - {book.title}")
        self.cancel_button.pack(side="left",padx=5, pady=5)
        self.add_button.configure(text="Save Changes")
        self.title_label.configure(text="🟡 Editing Book")
        self.available_checkbox.deselect()
        self.available_checkbox.configure(state="disabled")  

    def exit_edit_mode(self):
        self.current_book = None
        self.add_button.configure(text="Add Book")
        self.cancel_button.pack_forget()
        self.title("Library Management System")
        self.title_label.configure(text="Library Management System")

    def cancel_edit(self):
        self.reset_form()


    def reset_form(self):
        self.clear_entries()
        self.focus_set()
        self.available_checkbox.configure(state="normal") 
        self.exit_edit_mode()
        self.set_status("Edit cancelled.")


    def delete_book(self, book):
        if messagebox.askyesno("Delete Book", f"Delete '{book.title}'?"):
            if self.library.delete_book(book):
                self.refresh()
                self.set_status(f"🗑️ '{book.title}' deleted.")
    
    def return_book(self, book):
        if book.return_book():
            self.refresh()
            self.set_status(f"📗 Returned '{book.title}'.")
        else:
            self.set_status(f"'{book.title}' is already available.")

    def set_status(self, messsage):
        self.status_label.configure(text=messsage)

    def clear_entries(self):
        entries = [self.title_entry, self.author_entry, self.pages_entry, self.year_entry]
        for entry in entries:
            entry.delete(0, "end")

    def fill_entries(self, book):
        self.title_entry.insert(0, book.title)
        self.author_entry.insert(0, book.author)
        self.pages_entry.insert(0, str(book.pages))
        self.year_entry.insert(0, str(book.year))

    def refresh(self):
        self.sort_books(self.sort_menu.get())
        self.library.save()
        self.update_book_list(self.search_entry.get().strip().lower())

