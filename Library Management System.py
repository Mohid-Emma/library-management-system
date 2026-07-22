import json

class Book:
    def __init__(self, title, author, pages, year, available):
        if pages <= 0:
            raise ValueError("Pages must be positive.")
        if year <= 0:
            raise ValueError("Year must be positive.")
        
        self.title     = title 
        self.author    = author
        self.pages     = pages
        self.year      = year
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed successfully.")
            return
        print(f"{self.title} already borrowed.")
        
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} returned successfully.")
            return
        print(f"{self.title} is already in library.")

    def to_dict(self):
        return{"Title":self.title, "Author":self.author, "Pages":self.pages, "Year":self.year, "Available":self.available}

    def __str__(self):
        status = "Yes" if self.available else "No"
        return f"\nTitle     : {self.title}\nAuthor    : {self.author}\nPages     : {self.pages}\nYear      : {self.year}\nAvailable : {status}"
        
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title  == other.title and
                self.author == other.author and
                self.pages  == other.pages and
                self.year   == other.year)
    
    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages
    
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if self.find_book(book.title):
            print("Book already exists.")
            return
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("Book not available.")
            return
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.casefold() == title.casefold():
                return book
        return None

    def search_book(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"{title} was not found.")
            return
        print(book) 

    def borrow(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"{title} was not found.")
            return
        book.borrow()
        print(book)     

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"{title} was not found.")
            return
        book.return_book()
        print(book)

    def delete(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"{title} was not found.")
            return
        self.books.remove(book)
        print(f"{title} deleted successfully.")


    def save(self):
        data = [book.to_dict() for book in self.books]
        with open("Book_record.json", "w") as write_file:
            json.dump(data, write_file, indent=4)

    def from_dict(self):
        self.books.clear()
        try:
            with open("Book_record.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("Book_record.json", "x") as create_file:
                return
        except json.JSONDecodeError:
            return
        else:
            for item in data:
                available = item["Available"]
                self.books.append(Book(item['Title'], item['Author'], item['Pages'], item['Year'], available))
        

library = Library()
library.from_dict()

def check_integer(value, field="Value"):
    try:
        return int(value)
    except ValueError:
        print(f"{field} must be an integer number")

def add_book():
    title = input("Write the title of the book:\n")
    author = input("Who is the author of the book:\n")
    pages = input("Write the total number of pages of the book:\n")
    year = input("Which year was the book released:\n")
    available = input("Is book currently available:\n").lower()
    pages = check_integer(pages, "Pages")
    year = check_integer(year, "Year")
    if pages is None or year is None:
        return

    available = available == "yes"
    try:
        library.add_book(Book(title,author,pages,year,available))
    except ValueError as data:
        print(data)

def search_book():
    library.show_books()
    title = input("Write the title of the book you're looking for:\n")
    library.search_book(title)

def borrow_book():
    library.show_books()
    title = input("Write the title of the book you're borrow:\n")
    library.borrow(title)

def return_book():
    library.show_books()
    title = input("Write the title of the book you're return:\n")
    library.return_book(title)

def delete_book():
    library.show_books()
    title = input("Write the title of the book you're delete:\n")
    library.delete(title)


while True:
    print()
    print("1.Add Book")
    print("2.Show Books")
    print("3.Search Book")
    print("4.Borrow Book")
    print("5.Return Book")
    print("6.Delete Book")
    print("7.Exit")

    menu = {1:add_book, 2:library.show_books, 3:search_book, 4:borrow_book, 5:return_book, 6:delete_book}
    choice = input("Choose between 1 to 7:\n")
    choice = check_integer(choice, "Choice")
    if choice is None:
        continue
    if choice == 7:
        break
    menu.get(choice, lambda:print("Write only option from 1 to 7"))()

library.save()
