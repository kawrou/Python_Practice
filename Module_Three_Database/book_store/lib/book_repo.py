from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            obj = Book(row["id"], row["title"], row["author_name"])
            books.append(obj)
        return books