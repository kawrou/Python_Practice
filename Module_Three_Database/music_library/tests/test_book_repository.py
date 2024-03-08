from lib.book_repository import BookRepository
from lib.book import Book


"""
When I have a database with a table filled with data about books
and I call the all method from the BookRepository class
I will get a list of instances of book returned 
"""
def test_return_list_of_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    books = repo.all()
    
    assert books == [
        Book(1,'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3,'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

