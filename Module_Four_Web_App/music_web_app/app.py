import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app) 
    repository = AlbumRepository(connection)
    albums = repository.all()
    album_strings = [f"{album}" for album in albums]
    return "\n".join(album_strings)

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    repository.create(album)
    return "Album created successfully"

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all_artist_names()
    artists_string = [f"{artist}" for artist in artists]
    return ", ".join(artists_string)
    
@app.route('/artists', methods=['POST'])
def create_new_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    if 'name' not in request.form:
        return "You didn't enter any artist information", 400
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return "Artist added successfully"


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

