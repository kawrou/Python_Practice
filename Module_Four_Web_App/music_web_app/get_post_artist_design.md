# Single Table Design Recipe
1. Extract nouns from the user stories or specification
USER STORY:
'''
As a music lover,
I want to keep a list of music artists and their names.

As a music lover,
I want to keep a list of music artists and their genre

As a music lover,
I want to see a list of all the music artists I listen to. 

As a music lover,
I want to add a new artist, their name and genre to my list of artists

The artists_id should be connected with their associated albums. 

'''
Nouns: name, genre

2. Infer the Table Name and Columns
Name of the table (always plural): artists
Column names: id, name, genre

3. Decide the column types
name : text
genre : text


4. Write the SQL
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  name text,
  genre text,
);

5. Create the table
psql -h 127.0.0.1 music_web_app < artist_table.sql


# Route Design Recipe
1. Design the Route Signature
- GET Artists route
GET /artists

- POST Artists route
POST /artists
  name: Wild Nothing
  genre: Indie

2. Create Examples as Tests

"""
When I make a request to get all artists
I get served a list of all artists in my database. 
"""
#Expected response (200 OK)
#Return: Pixies, Abba, Taylor Swift, Nina Simone


"""
When I add a new artist to my database
Return (200 OK) and a message telling me it was succesful
"""
#Expected response (200 OK)
#Return: "Artist added succesfully"


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

"""
When I add a new artist with POST without a body parameter
I should receieve a (400) and "You didn't enter any artist information"

"""

3. Test-drive the Route
def test_get_all_artist(web_client):
    response - web_client.get("/artists)
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, Abba, Taylor Swift, Nina Simone"

def test_post_new_artist(web_client):
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8) == "Artist added successfully"

def test_post_new_artist_and_return_list_with_new_artist_added(web_client):
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, Abba, Taylor Swift, Nina Simone"
    response = web_client.post("/artists", data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8) == "Artist added successfully"
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8) == "Pixies, Abba, Taylor Swift, Nina Simone, Wild Nothing"

def test_post_artist_without_body_parameter(web_client):
    response = web_client.post("/artists)
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "You didn't enter any artist information"

