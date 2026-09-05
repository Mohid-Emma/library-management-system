#helper.py

import ctypes, tkinter , sys
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
    BASE_DIR = Path.home() / "Library Management System"
    BASE_DIR.mkdir(exist_ok=True)
    return BASE_DIR / "library.db"

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
# Icon Path
# =============================================================

def icon_location() -> Path:
    if getattr(sys, "frozen", False):
        BASE_DIR = Path(sys._MEIPASS)
    else:
        BASE_DIR = Path(__file__).resolve().parent.parent

    return BASE_DIR / "assets" /"icon.png"

# =============================================================
# Icon Extract
# =============================================================
def icon_extract(window) -> None:

    icon_path =  icon_location()

    if not icon_path.is_file():
        messagebox.showerror("Error", f"Warning: '{icon_path}' not found in the script directory.\n"+" "*100)
        return

    def apply_icon():
        window.icon_img = tkinter.PhotoImage(file=str(icon_path))
        window.iconphoto(False, window.icon_img)
        
    window.after(200, apply_icon)