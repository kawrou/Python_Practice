from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist

class Application():
    def __init__(self):
        # Connect to the database

        # My comment:
        # DatabaseConnection is just a name of a class that is using psycopg library
        # Creates an instance of the class DatabaseConnection
        self._connection = DatabaseConnection()
        self._connection.connect()

        # Seed with some seed data

        # My comment:
        # Uses the "seed" method from DatabaseConnection to open, read, and seed the data in the sql file. 
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        user_input = int(input('What would you like to do?\n'
                        '1 - List all artists\n'
                        '2 - Find artist by ID\n'
                        '3 - Add new artist\n'
                        '4 - Delete artist\n'
                        '5 - List all albums\n'
                        '6 - Find album by ID \n'
                        '7 - Add new album\n'
                        '8 - Delete album by ID\n'
                        'Enter your choice: '))
        
        # My comment:
        # Create an instance of the class ArtistReposistory 
        # Creates a connection between the Artist Repository Class Object and the database so that the data is accesible.
        artist_repository = ArtistRepository(self._connection)
        album_repository = AlbumRepository(self._connection)

        if user_input == 1:
            # Retrieve all artists
            # Calls the all method and stores the list of artist data as individual objects from the artist class in a variable
            artists = artist_repository.all()
            # List them out
            for artist in artists:
                print(artist)

        if user_input == 2:
            artist_id = int(input("Enter artist id: "))
            artist = artist_repository.find(artist_id)
            print(artist)

        if user_input == 3:
            artist_name = input("Enter artist name: ")
            artist_genre = input("Enter artist's genre: ")

            artist_repository.create(Artist(None, artist_name, artist_genre))
            print("Artist added succesfully")

        if user_input == 4:
            artist_id = int(input("Enter artist ID: "))
            artist_repository.delete(artist_id)
            print("Artist deleted successfully")

        if user_input == 5:
            albums = album_repository.all()
            for album in albums:
                print(album)

        if user_input == 6:
            album_id_search_input = int(input("Enter album id: "))
            album = album_repository.find(album_id_search_input)
            print(album)

        if user_input == 7:
            album_title = input("Enter album title: ")
            album_release_year = int(input("Enter release year: "))
            artist_id = int(input("Enter artist ID: "))

            album_repository.create(Album(None,album_title, album_release_year, artist_id))
            print("Album created successfully")

        if user_input == 8:
            album_id = int(input("Enter album ID: "))   
            album_repository.delete(album_id)
            print("Album deleted successfully") 


if __name__ == '__main__':
    app = Application()
    app.run()
