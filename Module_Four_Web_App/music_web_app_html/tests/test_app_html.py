from playwright.sync_api import Page, expect
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

# def test_get_all_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     AlbumRepository(db_connection)
#     page.goto(f"http://{test_web_address}/albums")
#     album_title = page.locator("h4")
#     expect(album_title).to_contain_text([
#         "Title: Doolittle",
#         "Title: Surfer Rosa",
#         "Title: Waterloo",
#         "Title: Super Trouper",
#         "Title: Bossanova",
#         "Title: Lover",
#         "Title: Folklore",
#         "Title: I Put a Spell on You",
#         "Title: Baltimore",
#         "Title: Here Comes the Sun",
#         "Title: Fodder on My Wings",
#         "Title: Ring Ring"
#     ])
#     album_year = page.locator("p")
#     expect(album_year).to_contain_text([
#         "Released: 1989",
#         "Released: 1988",
#         "Released: 1974",
#         "Released: 1980",
#         "Released: 1990",
#         "Released: 2019",
#         "Released: 2020",
#         "Released: 1965",
#         "Released: 1978",
#         "Released: 1971",
#         "Released: 1982",
#         "Released: 1973"
#     ])

# FAILING TEST

def test_get_all_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    AlbumRepository(db_connection)
    page.goto(f"http://{test_web_address}/albums")
    albums = page.locator("div")
    print(albums)
    expect(albums).to_contain_text([
        'Title: Doolittle Released: 1989',
        'Title: Surfer Rosa Released: 1988',
        'Title: Waterloo Released: 1974',
        'Title: Super Trouper Released: 1980',
        'Title: Bossanova Released: 1990',
        'Title: Lover Released: 2019',
        'Title: Folklore Released: 2020',
        'Title: I Put a Spell on You Released: 1965',
        'Title: Baltimore Released: 1978',
        'Title: Here Comes the Sun Released: 1971',
        'Title: Fodder on My Wings Released: 1978',
        'Title: Ring Ring Released: 1973'
    ])

def test_get_single_album_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    AlbumRepository(db_connection)
    page.goto(f"http://{test_web_address}/albums/1")
    album_title = page.locator("h1")
    expect(album_title).to_contain_text(["Album: Doolittle"])
    album_year = page.locator("p")
    expect(album_year).to_contain_text(["Released: 1989\nArtist: Pixies"])


"""
When I am on the albums list page
There will be links from each album to their own album page that contains release year and artist
When I click on that link '/albums/<id>, I'll be forwarded to that specific album page
"""

def test_link_from_albums_list_to_individual_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    AlbumRepository(db_connection)
    page.goto(f"http://{test_web_address}/albums")
    albums = page.locator("li")
    expect(albums).to_contain_text([
        'Doolittle',
        'Surfer Rosa',
        'Waterloo',
        'Super Trouper',
        'Bossanova',
        'Lover',
        'Folklore',
        'I Put a Spell on You',
        'Baltimore',
        'Here Comes the Sun',
        'Fodder on My Wings',
        'Ring Ring'
    ])
    page.click("text = Doolittle")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_contain_text('Album: Doolittle')
    album_info = page.locator("p")
    expect(album_info).to_contain_text(["Released: 1989\nArtist: Pixies"])


"""
When I make a request with GET /artist/<id>
I will receive an html page displaying the relevant information pertaining to that id (i.e. artist name, genre)
GET /artist/1 => Pixies, Rock
"""
def test_get_artist_by_id(test_web_address, page, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_contain_text(["Pixies"])
    artist_genre = page.locator("p")
    expect(artist_genre).to_contain_text(["Rock"])

def test_get_artist_by_id_4(test_web_address, page, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    page.goto(f"http://{test_web_address}/artists/4")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_contain_text(["Nina Simone"])
    artist_genre = page.locator("p")
    expect(artist_genre).to_contain_text(["Jazz"])


"""
When I make a request with GET/artists
I will receive an html page displaying the list of artists in my database
There will be a link to the artist's individual page for each artist in the list
When I click on that link, I will be sent to the relevant page
GET/artists => Pixies, ABBA, ... => Pixies, Rock
"""
def test_get_artist_list(test_web_address, page, db_connection):
    db_connection.seed("seeds/music_library.sql")
    ArtistRepository(db_connection)
    page.goto(f"http://{test_web_address}/artists")
    li_tag = page.locator("li")
    expect(li_tag).to_contain_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])
    page.click("text = Pixies")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_contain_text(["Pixies"])
    artist_genre = page.locator("p")
    expect(artist_genre).to_contain_text(["Rock"])
