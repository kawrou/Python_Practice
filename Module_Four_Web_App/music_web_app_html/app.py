import os
from flask import Flask, request, render_template
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app) 
#     repository = AlbumRepository(connection)
#     albums = repository.all()
#     for album in albums:
#         print(album.title)
#     album_strings = [f"{album}" for album in albums]
#     return "\n".join(album_strings)
    
    
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

# @app.route('/artists', methods=['GET'])
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all_artist_names()
#     artists_string = [f"{artist}" for artist in artists]
#     return ", ".join(artists_string)
    
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

#------------------FOR HTML-----------------------------

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app) 
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums = albums)

@app.route('/albums/<id>')
def get_single_album_and_its_artist(id):
    connection = get_flask_database_connection(app) 
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    return render_template('albums/album.html', album = album, artist = artist)

@app.route('/artists/<id>')
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template('artists/artist.html', artist = artist)

@app.route('/artists')
def get_artist_list():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('artists/index.html', artists = artists)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
