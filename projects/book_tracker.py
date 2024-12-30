class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre
        self.read = False

    def mark_as_read(self):
        self.read = True

    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"'{self.title}' by {self.author} (Genre: {self.genre}) - {status}"


class BookTracker:
    def __init__(self):
        self.books = []

    def add_book(self, new_book: Book):
        self.books.append(new_book)

    def view_books(self):
        if not self.books:
            print("No books in your collection yet!")
        else:
            print("\nYour Book Collection:")
            for book in self.books:
                print(book)

    def mark_book_as_read(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Book '{title}' marked as read!")
                return
        print(f"No book found with the title '{title}'.")

    def _filter(self, by: str, value: str):
        if by not in ["author", "genre"] and hasattr(Book, by):
            raise ValueError("Invalid 'by' selected for filtering")

        filtered_books = []
        for book in self.books:
            if getattr(book, by).lower() == value.lower():
                filtered_books.append(book)

        if not filtered_books:
            print(f"No books found with {by} '{value}'.")
        else:
            print(f"\nBooks with {by} '{value}':")
            for book in filtered_books:
                print(book)

        return filtered_books

    def filter_books_by_author(self, author: str):
        self._filter("author", author)

    def filter_books_by_genre(self, genre: str):
        self._filter("genre", genre)
