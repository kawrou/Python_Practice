from playwright.sync_api import Page, expect
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
# Tests for your routes go here


# Tests for your routes go here


def test_get_all_albums_from_database(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    AlbumRepository(db_connection)
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''\
        'Album(1, Doolittle, 1989, 1)\n' \
        'Album(2, Surfer Rosa, 1988, 1)\n'\
        'Album(3, Waterloo, 1974, 2)\n' \
        'Album(4, Super Trouper, 1980, 2)\n' \
        'Album(5, Bossanova, 1990, 1)\n' \
        'Album(6, Lover, 2019, 3)\n' \
        'Album(7, Folklore, 2020, 3)\n' \
        'Album(8, I Put a Spell on You, 1965, 4)\n' \
        'Album(9, Baltimore, 1978, 4)\n' \
        'Album(10, Here Comes the Sun, 1971, 4)\n' \
        'Album(11, Fodder on My Wings, 1982, 4)\n' \
        'Album(12, Ring Ring, 1973, 2)'


def test_post_new_album_and_return_new_album_list(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    AlbumRepository(db_connection)
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album created successfully"
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''\
        'Album(1, Doolittle, 1989, 1)\n' \
        'Album(2, Surfer Rosa, 1988, 1)\n'\
        'Album(3, Waterloo, 1974, 2)\n' \
        'Album(4, Super Trouper, 1980, 2)\n' \
        'Album(5, Bossanova, 1990, 1)\n' \
        'Album(6, Lover, 2019, 3)\n' \
        'Album(7, Folklore, 2020, 3)\n' \
        'Album(8, I Put a Spell on You, 1965, 4)\n' \
        'Album(9, Baltimore, 1978, 4)\n' \
        'Album(10, Here Comes the Sun, 1971, 4)\n' \
        'Album(11, Fodder on My Wings, 1982, 4)\n' \
        'Album(12, Ring Ring, 1973, 2)\n' \
        'Album(13, Voyage, 2022, 2)'
    
"""
When I make a request to get all artists
I get served a list of all artists in my database. 
"""
#Expected response (200 OK)
#Return: Pixies, Abba, Taylor Swift, Nina Simone

def test_get_all_artist(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I add a new artist to my database
Return (200 OK) and a message telling me it was succesful
"""
#Expected response (200 OK)
#Return: "Artist added succesfully"
def test_post_new_artist(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist added successfully"

'''
When I make a request to get all artists
I recieve a list of all artist in DB
Then I add a new artist to my database and make a request for all artists
I expect to receive a list with the new artist added.  
'''
#Expected response (200 OK)
#Return: Pixies, Abba, Taylor Swift, Nina Simone
#Exptected response (200 OK)
#Return: "Artist added succesfully"
#Expected response (200 OK)
#Return: Pixies, Abba, Taylor Swift, Nina Simone, Wild Nothing, 

def test_post_new_artist_and_return_list_with_new_artist_added(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist added successfully"
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing"


def test_post_artist_without_body_parameter(web_client,  db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    response = web_client.post("/artists")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "You didn't enter any artist information"

