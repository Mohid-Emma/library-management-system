#library.py
import json
from models.book import Book, Borrower
from utils.helpers import file_location
    
class Library:
    def __init__(self) -> None:
        self.books : list[Book] = []
        self.data_file = file_location()

    def find_book(self, title : str) -> Book | None:
        for book in self.books:
            if book.title.casefold() == title.casefold():
                return book
        return None

    def add_book(self, book : Book) -> bool:
        if self.find_book(book.title):
            return False
        self.books.append(book)
        return True

    def delete_book(self, book : Book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False
    
    def save(self) -> None:
        data = [book.to_dict() for book in self.books]
        with self.data_file.open("w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=5, ensure_ascii=False)


    def load(self) -> None:
        self.books.clear()
        try:
            with self.data_file.open("r", encoding="utf-8") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            self.data_file.write_text("[]", encoding="utf-8")
            return
        except json.JSONDecodeError:
            self.data_file.write_text("[]", encoding="utf-8")
            return
        else:
            for item in data:
                try:
                    book = Book(item['Title'], item['Author'], item['Pages'], item['Year'], item["Available"])
                    borrower_name = item.get("Borrower")
                    if borrower_name:
                        book.borrower = Borrower(borrower_name)
                        book.available = False

                    self.books.append(book)

                except(KeyError, ValueError):
                    continue