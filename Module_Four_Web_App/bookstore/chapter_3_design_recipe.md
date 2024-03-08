1. Route Signature

# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

#sort-names Route
POST /sort-names
    names: string
    message: string

2. Create Examples as tests
#Example

"""
When: I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter text
Then: I should get a 200 response with a string of alphabetically sorted names
"""
Post /sort-names
    Parameters:
        names: Joe,Alice,Zoe,Julia,Kieran
        return: Alice,Joe,Julia,Kieran,Zoe
    Expected response (200 ok):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

"""
When: I make a POST request to /sort-names
And: I send nothing as the body parameter text
Then: I should get a 400 response
"""
Post /sort-names
    Parameters:
        names: None
    Expected response (400 Bad Request)
"""
Please provide names
"""

"""
When: I make a POST request to /sort-names
And: I send only 1 name in the string in the body parameter text
Then: I should get a 200 response and a string containing only one name
"""
Post /sort-names
    Parameters:
        names: Joe
    Expected response (200 ok):

