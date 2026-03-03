class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True   # Book is available by default

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to library.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} has been issued.")
                return
        print(f"{title} is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"{title} has been returned.")
                return
        print(f"{title} was not issued.")

    def display_books(self):
        for book in self.books:
            print(book)

#Create library
library = Library()

# Create books
book1 = Book("Python Basics", "Ali Aslam")
book2 = Book("OOP Concepts", "Jane Smith")

# Add books
library.add_book(book1)
library.add_book(book2)

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Basics")

# Return a book
library.return_book("Python Basics")

# Display books again
library.display_books()