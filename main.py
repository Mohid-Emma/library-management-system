#main.py

from database import Database
from frontend import MainWindows, BookForm, BookView, BookCard, StatusBar, BorrowerDialog
from controller import LibraryApp
from backend import Library

ui_compounds = {
   "form"   : BookForm, 
   "view"   : BookView,
   "card"   : BookCard, 
   "status" : StatusBar, 
   "dialog" : BorrowerDialog }


# =============================================================
#  Program Initiallization
# =============================================================

def main() -> None:
    app = LibraryApp(
        main_window = MainWindows, 
        ui_compounds = ui_compounds,
        database = Database,
        library = Library)
    app.run()

if __name__ == "__main__":
    main()