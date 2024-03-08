from lib.album_repository import AlbumRepository
from lib.album import Album


def test_get_all_records(db_connection):
    """
    When we call AlbumRepository#all
    We get a list of Album objects reflecting the seed data.
    """
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()  # get all albums

    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
    ]

def test_find_album_by_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    respository = AlbumRepository(db_connection)

    album = respository.find(2)

    assert album == Album(2, "Surfer Rosa", 1988, 1)

"""
When we call AlbumRepository#create
We get a new record in the database
"""
def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None,"Trome Le Monde", 1991, 1))

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1), 
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2), 
        Album(5,'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7,'Folklore', 2020,3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978,4), 
        Album(10,'Here Comes the Sun', 1971, 4), 
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973,2),
        Album(13,'Trome Le Monde', 1991, 1),
    ]


def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None,"Trome Le Monde", 1991, 1))
    
    album_by_id = repository.find(13)
    assert album_by_id == (Album(13,'Trome Le Monde', 1991, 1))

    repository.delete(13)
    all_albums = repository.all()
    assert all_albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1), 
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2), 
        Album(5,'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7,'Folklore', 2020,3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978,4), 
        Album(10,'Here Comes the Sun', 1971, 4), 
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973,2),
    ]
