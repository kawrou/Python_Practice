from lib.album import Album


def test_album_constructs():
    """
    Album constructs with an id, title, release_year, artist_id
    """
    album = Album(1, "The white album", 1968, 5)
    assert album.id == 1
    assert album.title == "The white album"
    assert album.release_year == 1968
    assert album.artist_id == 5


def test_albums_are_equal():
    """
    We can compare two identical albums and assert them to equal
    """
    album1 = Album(1, "test title", "test release", "test artist_id")
    album2 = Album(1, "test title", "test release", "test artist_id")
    assert album1 == album2


def test_album_format():
    """
    We can format albums to strings nicely
    """
    album1 = Album(1, "test title", "test release", "test artist_id")
    assert str(album1) == "Album(1, test title, test release, test artist_id)"
