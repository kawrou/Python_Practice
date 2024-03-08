1. Design and create the table if needed. 
    N/A

2. Create test SQL seeds.
    N/a

3. Define the Model and Repository class names.
4. Implement the Model class.
    Table Name: books
    
    Model class
    in (lib/book.py)
    ```python
    class Book:
        def __init__(self):
            self.id = 0
            self.title = ""
            self.author_name = ""
    ```

  

3. Define the Model and Repository class names.    
5. Design the Repository class interface.
    Repository class
    in (lib/book_repo.py)
    
    ```python
    class BookRepository:
        def __init__(self):
            self._conection = conection
        #Selecting all records
        #No args
        def all(self):
            #Executes the SQL query
            #SELECT id, title, author_name FROM books
            #returns an array of book objects
            pass
    ```


6. Write test examples. 
    ```python
    
    
    
    """
    When I have a database with a table filled with data about books
    and I call the all method from the BookRepository class
    I will get a list of instances of book returned 
    """
    def test_return_list_of_books(db_connection):
        db_connection.seed("seeds/book_store.sql")
        repo = BookRepository(db_connection)
        books = repo.all()
        assert books == a list containing all the instances of books

    """
    When I construct a Book
    With the fields id, title, author_name
    They are reflectd in the instance's properties
    """
    def test_constructs_book():
        book = Book(1, "Nineteen Eighty-Four", "George Orwell")
        assert book.id == 1
        assert book.title == "Nineteen Eight-Four"
        assert book.author_name == "George Orwell"
    ```


7. Test-drive and implement the Repository class behaviour. 
