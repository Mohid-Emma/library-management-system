#borrower.py

class Borrower:
    def __init__(self, name: str) -> None:

        name = name.strip()
    # =============================================================
    # Custom Exception
    # =============================================================

        if len(name) < 2:
            raise ValueError("Name should be at least 2 characters long."+ " "*10)
        if len(name) > 30:
            raise ValueError("Name is too long.")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Only letters are allowed.")
    # =============================================================
    # Name Assignation
    # =============================================================

        self.name = name

# =============================================================
# Convert into String form
# =============================================================

    def __str__(self) -> str:
        return self.name
    