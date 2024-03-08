# Tests for your routes go here
# File: tests/test_app.py

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'


"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter text
Then: I should get a 200 response with a string of alphabetically sorted names
"""
"""
Post /sort-names
    Parameters:
        names: Joe,Alice,Zoe,Julia,Kieran
        return: Alice,Joe,Julia,Kieran,Zoe
    Expected response (200 ok):
    Return: Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names_returns_sorted(web_client):
    response = web_client.post('/sort-names', data = {'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a POST request to /sort-names
And: I send only 1 name in the string in the body parameter text
Then: I should get a 200 response and a string containing only one name
"""
"""
Post /sort-names
    Parameters:
        names: Joe
    Expected response (200 ok):
"""
def test_post_sort_names_for_one_name(web_client):
    response = web_client.post('/sort-names', data = {'names': 'Joe'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Joe'

"""
Post /sort-names
    Parameters: 
        names: Aaaaaa, Aaaaaz, Aaaaab
    Expeted response (200 OK)
    Return: Aaaaaa,Aaaaab,Aaaaaz
"""
def test_post_sort_names_for_same_starting_letter(web_client):
    response = web_client.post('/sort-names', data = {'names': 'Aaaaaa,Aaaaaz,Aaaaab'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaaa,Aaaaab,Aaaaaz'

"""
When: I make a POST request to /sort-names
And: I send nothing as the body parameter text
Then: I should get a 400 response
"""
"""
Post /sort-names
    Parameters:
        names: None
    Expected response (400 Bad Request)
    Return: Please provide names
"""
def test_post_sort_names_with_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide names'

"""
When: I make a GET request to /add
And: I send "Eddie" as the body parameter text
Then: I should get a 200 response with a string of names with Eddied added to the end. 
"""
"""
Post /add
    Parameters:
        name: Eddie
    Expected response (200 ok):
    Return: Julia,Alice,Karim,Eddie
"""

def test_get_add_name_to_pre_defined_list(web_client):
    response = web_client.get('/add?name=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie'

"""
When: I make a GET request to /add
And: I send have no parameters
Then: I should get a 400 response with "You did not input a name to add"
"""
"""
Post /add
    Parameters:
    Expected response (400 Bad Request):
    Return: "You did not input a name to add"
"""

def test_get_add_with_no_name_added_to_pre_defined_list(web_client):
    response = web_client.get('/add')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'You did not input a name to add'    


"""
When: I make a GET request to /add
And: I send "Henry" as the body parameter text
Then: I should get a 200 response with a string of names with Henry added to the end. 
"""
"""
Post /add
    Parameters:
        name: Eddie
    Expected response (200 ok):
    Return: Julia,Alice,Karim,Henry
"""

def test_get_add_name_Henry_to_pre_defined_list(web_client):
    response = web_client.get('/add?name=Henry')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Henry'

def test_get_add_multiple_names_to_pre_defined_list(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
