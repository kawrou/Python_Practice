1. Route Signature

# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

#add Route
GET /add
    name: Eddie


2. Create Examples as tests
#Example

"""
When: I make a GET request to /add
And: I send "Eddie" as the body parameter text
Then: I should get a 200 response with a string of names with Eddied added to the end. 
"""
Post /add
    Parameters:
        name: Eddie
        return: Julia, Alice, Karim, Eddie
    Expected response (200 ok):
"""
Julia, Alice, Karim, Eddie
"""



