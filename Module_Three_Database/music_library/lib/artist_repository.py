from lib.artist import Artist
from lib.album import Album

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
        
    # My comments:
    # Uses the psycopg connection to execute SQL queries
    # Stores the data in the rows variable which is a list of dicts, the keys are the column headers. 
    # Calls the Artist class and places the data into the class's attributes for each row in the table
    # Append the Artist class objects into the artists list
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find a single artist by their id

    # Similar to the above
    # There should only be a single row from the SQL query as unique artist_id
    # Turns the first row of the queried table into a variable
    # Returns the Artist object for the single artist 
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
            artist.name, artist.genre])
        return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None

    #Find all albums by artist
    # def find_with_albums(self, artist_id):
    #     rows = self._connection.execute(
    #         "SELECT artists.id AS artist_id, artists.name, artists.genre, albums.id AS album_id, albums.title, albums.release_year " \
    #         "FROM artists JOIN albums ON artists.id = albums.artist_id " \
    #         "WHERE artists.id = %s", [artist_id])
    
    def find_with_albums(self, artist_id):
        rows = self._connection.execute(
            'SELECT artists.id AS artist_id, artists.name, artists.genre, albums.id AS album_id, albums.title, albums.release_year '\
            'FROM artists '\
            'JOIN albums ON artists.id = albums.artist_id '\
            'WHERE artists.id = %s', [artist_id])
    
    
    
        albums = []
        for row in rows:
            album = Album(row["album_id"], row["title"],  row["release_year"], row["artist_id"])
            albums.append(album)
        return Artist(rows[0]['artist_id'], rows[0]["name"], rows[0]["genre"], albums)
    
