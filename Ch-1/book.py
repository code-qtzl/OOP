class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        # checking library_book in books list
        for library_book in self.books:
            # checking if the library books are matching the title and author value
            if library_book.title == book.title and library_book.author == book.author:
                # if they do, then remove that library_book
                self.books.remove(library_book)
                return 

    def search_books(self, search_string):
        # converting to lower case
        search_string = search_string.lower()
        matching = []

        for book in self.books:
            if (search_string in book.title.lower() or
                    search_string in book.author.lower()):
                matching.append(book)
        return matching