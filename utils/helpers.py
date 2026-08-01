#helper.py
from pathlib import Path
from tkinter import messagebox

def check_integer(value: str, field: str="Value") -> int | None:
    try:
        return int(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{field} must be an integer number")
        return None 
    

def file_location() -> Path:
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_dir = BASE_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "Book_record.json"
