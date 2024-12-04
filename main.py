class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed the book: {self.title}")
        else:
            print(f"Sorry, the book '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"You returned the book: {self.title}")


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Book '{book_title}' removed from the library.")
                return
        print(f"Book '{book_title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f" - {book.title} by {book.author} ({book.year})")
        else:
            print("No books available for borrowing.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                if book.is_available:
                    book.borrow()
                    return
                else:
                    print(f"The book '{book_title}' is currently unavailable.")
                    return
        print(f"Book '{book_title}' not found in the library.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                book.return_book()
                return
        print(f"Book '{book_title}' not found in the library.")