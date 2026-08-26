#main.py

from gui      import LibraryApp
from database import Database

# =============================================================
#  Program Initiallization
# =============================================================

def main():
    db  = Database()
    db.create_table()
    app = LibraryApp(db)
    app.mainloop()

if __name__ == "__main__":
    main()