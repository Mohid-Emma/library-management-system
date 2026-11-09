#main.py

from database import Database
from frontend import MainWindows, Form, View, Card, StatusBar, Dialog
from controller import LibraryApp
from backend import Library

ui_compounds = {
   "form"   : Form,
   "view"   : View,
   "card"   : Card, 
   "status" : StatusBar, 
   "dialog" : Dialog }


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