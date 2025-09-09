class Library:
    def __init__(self, books):
        self.books = books

    def borrow(self, title):
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            return f"You borrowed {title}"
        else:
            return f"Sorry, {title} is not available"

    def return_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1
        return f"You returned {title}"

    def show_books(self):
        print("Available books:", self.books)


lib = Library({"Python 101": 3, "Data Science": 2})

print(lib.borrow("Python 101"))
print(lib.return_book("Python 101"))
lib.show_books()
