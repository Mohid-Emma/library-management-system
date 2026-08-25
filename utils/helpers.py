#helper.py
from pathlib import Path
from tkinter import messagebox
from models  import Book

def check_integer(value: str, field: str="Value") -> int | None:
    try:
        return int(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{field} must be an integer number")
        return None 
    

def file_location() -> Path:
    BASE_DIR = Path(__file__).resolve().parent.parent
    return BASE_DIR / "database" /"library.db"
    
def check_for_borrower(book: Book) -> str | None:
    return book.borrower.name if book.borrower else None