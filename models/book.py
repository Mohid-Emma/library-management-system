# book.py
from .borrower import Borrower

class Book:
    def __init__(self, title, author, pages, year, available= True, book_id= None) -> None:
    # =============================================================
    # Custom Exception
    # =============================================================

        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author.strip():
            raise ValueError("Author cannot be empty.")
        if pages <= 0:
            raise ValueError("Pages must be positive.")
        if year <= 0:
            raise ValueError("Year must be positive.")

    # =============================================================
    # Object Assignation
    # =============================================================

        self.title     = title.strip() 
        self.author    = author.strip()
        self.pages     = pages
        self.year      = year
        self.available = available
        self.borrower  = None
        self.book_id   = book_id

# =============================================================
# Book Borrow
# =============================================================

    def borrow_name(self, borrower : Borrower) -> bool:
        if self.available:
            self.borrower  = borrower
            self.available = False
            return True
        return False

# =============================================================
# Book Return
# =============================================================

    def return_book(self) -> bool:
        if not self.available:
            self.borrower  = None
            self.available = True
            return True
        return False

# =============================================================
# Book Update
# =============================================================

    def update(self, other : "Book") -> None:
        self.title   =  other.title
        self.author  =  other.author
        self.pages   =  other.pages
        self.year    =  other.year

# =============================================================
# Book Data into Dictionary Form
# =============================================================

    def to_dict(self) -> dict:
        return{
            "Title"    :self.title, 
            "Author"   :self.author, 
            "Pages"    :self.pages, 
            "Year"     :self.year, 
            "Available":self.available, 
            "Borrower" :self.borrower.name if self.borrower else None}

# =============================================================
# Convert into String form
# =============================================================

    def __str__(self) -> str:
        return f"\nTitle     : {self.title}\nAuthor    : {self.author}\nPages     : {self.pages}\nYear      : {self.year}\nAvailable : {'Available' if self.available else 'Borrowed'}"
# =============================================================
# Object Comparation Method
# =============================================================        

    def __len__(self) -> int:
        return self.pages
    
    def __eq__(self, other : object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title  == other.title and
                self.author == other.author and
                self.pages  == other.pages and
                self.year   == other.year)
    
    def __gt__(self, other : object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages
    
    def __lt__(self, other : object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages
