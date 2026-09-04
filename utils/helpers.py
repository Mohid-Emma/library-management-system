#helper.py

import ctypes
import tkinter
from   pathlib import Path
from   models  import Book
from   tkinter import messagebox

# =============================================================
# Check for Integer form
# =============================================================

def check_integer(value: str, field: str="Value") -> int | None:
    try:
        return int(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{field} must be an integer number\n"+" "*100)
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
    return book.borrower if book.borrower else None

# =============================================================
# App Id
# =============================================================

def app_id() -> None:
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my_library_app")
    except Exception as e:
        messagebox.showerror("Error", f"Taskbar fix failed: {e}\n"+" "*100)
        return None

# =============================================================
# Check for Icon
# =============================================================

def check_for_icon() -> bool | Path | None:
    BASE_DIR  = Path(__file__).resolve().parent.parent
    icon_path =  BASE_DIR / "assets" /"icon.png"

    if icon_path.exists():
        return True, icon_path
    else:
        messagebox.showerror("Error", f"Warning: '{icon_path}' not found in the script directory.\n"+" "*100)
        return False, None
    
# =============================================================
# Icon Extract
# =============================================================
def icon_extract(window) -> None:

    icon_exist, icon_path = check_for_icon()
    if icon_path is None or not icon_exist:
        return

    def apply_icon():
        window.icon_img = tkinter.PhotoImage(file=str(icon_path))
        window.iconphoto(False, window.icon_img)
        
    window.after(200, apply_icon)