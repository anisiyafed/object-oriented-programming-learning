class Book:
    def __init__(self, title, author, genre):
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

    def add_book(self, new_book):
        self.books.append(new_book)

    def view_books(self):
        if not self.books:
            print("No books in your collection yet!")
        else:
            print("\nYour Book Collection:")
            for book in self.books:
                print(book)

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Book '{title}' marked as read!")
                return
        print(f"No book found with the title '{title}'.")

    def filter_books_by_author(self, author):
        filtered_books = []
        for book in self.books:
          if book.author.lower() == author.lower():
              filtered_books.append(book)
          
        if not filtered_books:
            print(f"No books found by the author '{author}'.")
        else:
            print(f"\nBooks by {author}:")
            for book in filtered_books:
                print(book)

    def filter_books_by_genre(self, genre):
        filtered_books = []
        for book in self.books:
          if book.genre.lower() == author.genre():
              filtered_books.append(book) 
        
        if not filtered_books:
            print(f"No books found in the genre '{genre}'.")
        else:
            print(f"\nBooks in Genre: {genre}:")
            for book in filtered_books:
                print(book)
