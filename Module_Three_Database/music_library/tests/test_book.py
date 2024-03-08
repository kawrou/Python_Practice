from lib.book import Book

"""
When I construct a Book
With the fields id, title, author_name
They are reflectd in the instance's properties
"""

def test_constructs_book():
    book = Book(1, 'Nineteen Eighty Four', 'George Orwell') 
    assert book.id == 1
    assert book.title == 'Nineteen Eighty Four'
    assert book.author_name ==  'George Orwell'

