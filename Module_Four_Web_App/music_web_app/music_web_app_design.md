# Single Table Design Recipe
1. Extract nouns from the user stories or specification
USER STORY:
'''
As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.

As a music lover, 
I want to see the album's artist reference

AS a music lover,
so I can add a new album,
i want to add a new album to my list of albums
'''
Nouns: title, release_year, artist_id

2. Infer the Table Name and Columns
Name of the table (always plural): albums
Column names: title, release_year, artist_id

3. Decide the column types
title : text
release_year : text
artist_id : INTEGER

4. Write the SQL
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year text,
  artist_id INTEGER
);
5. Create the table
psql -h 127.0.0.1 music_web_app < albums_table.sql


# Route Design Recipe
1. Design the Route Signature
- Waving route
GET /wave?name=<string>

- add album route
POST /albums
  title: Voyage
  release_year: 2022
  artist_id: 2

2. Create Examples as Tests

'''
I created a new album returns (200 OK)
Epected "Album created successfully"
'''

'''
When I create a new album
I expect GET /albums to return a list of albums with new album added. 
'''

3. Test-drive the Route
def test_created_new_album(web_client):
    response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode("utf-8) == "Album created successfully"

def test_new_album_added_to_table(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8) == ""