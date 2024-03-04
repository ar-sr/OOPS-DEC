class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.publication_year})")

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Library Books:")
            for book in self.books:
                book.display_info()

# Example Usage
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)

library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_books()

library.remove_book(book1)

library.display_books()
