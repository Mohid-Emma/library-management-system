#helper.py

from pathlib import Path
from models  import Book
from tkinter import messagebox

    # =============================================================
    # Check for Integer form
    # =============================================================

def check_integer(value: str, field: str="Value") -> int | None:
    try:
        return int(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{field} must be an integer number")
        return None 

    # =============================================================
    # File Path
    # =============================================================

def file_location() -> Path:
    BASE_DIR = Path(__file__).resolve().parent.parent
    return BASE_DIR / "database" /"library.db"

    # =============================================================
    # Check for Borrower
    # =============================================================

def check_for_borrower(book: Book) -> str | None:
    return book.borrower.name if book.borrower else None