# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages   # underscore = encapsulated (shouldn't be accessed directly)
        self.current_page = 0

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self._pages:
            self.current_page = self._pages
        return f"You are on page {self.current_page} of {self._pages}."


# Child class: EBook (inherits Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call parent constructor
        self.file_size = file_size  # in MB

    # Polymorphism: override get_info()
    def get_info(self):
        return f"'{self.title}' (E-Book) by {self.author}, {self._pages} pages, {self.file_size}MB."


# ----------------------
# Example usage:

book1 = Book("1984", "George Orwell", 328)
print(book1.get_info())              # '1984' by George Orwell, 328 pages.
print(book1.read(50))                # You are on page 50 of 328.

ebook1 = EBook("Python Crash Course", "PLP", 500, 5)
print(ebook1.get_info())             # Polymorphic version
print(ebook1.read(120))              # Inherited method still works
