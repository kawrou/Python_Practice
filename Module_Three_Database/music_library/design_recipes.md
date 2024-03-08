# Exercise design recipes:

## Challenge 2 - test driving model repository classes:
You have the code for handling the Artist data, now your assignment is to test-drive two new classes; an Album class and an AlbumRepository class with an all method, using the Design Recipe above.
- Work in the music_library project you created earlier.
- Test-drive an Album class that has attributes for each column in the albums table. You can find the table in seeds/music_library.sql.
- Test-drive an AlbumRepository class that has a method all that returns a list of Album objects.
- Write a small program in app.py using the class AlbumRepository to print out the list of albums to the terminal.

### Design and create the table if needed.
- Completed for us already

### Create test SQL seeds.
- Completed for us already

### Define the Model and Repository class names.
- Album
- AlbumRepository

### Implement the Model class.
- Album:
    - attributes
        - id
        - title
        - release_year
        - artist_id
    - methods:
        - __eq__
        - __repr__

### Design the Repository class interface.
- AlbumRepository:
    - attributes:
        - _connection
    - methods:
        - all

### Write test examples.

### Test-drive and implement the Repository class behaviour.
