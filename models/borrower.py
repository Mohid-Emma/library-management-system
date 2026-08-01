#borrower.py

class Borrower:
    def __init__(self, name: str) -> None:
        name = name.strip()
        if len(name) < 2:
            raise ValueError("Name should be at least 2 characters long.")
        if len(name) > 30:
            raise ValueError("Name is too long.")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Only letters are allowed.")
        self.name = name

    def __str__(self) -> str:
        return self.name
    