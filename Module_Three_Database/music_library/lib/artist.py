# My comments:
# This class is called from the ArtistRepository class.
# Each row of in the database is related to one artist
# That data from the individual artist is stored as an Artist object
# This is so that the data is turned into Python useable data. 


class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre, albums = []):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums
    
    # EQUALITY
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    
    # My comments:
    # The __eq__ dunder method compares two objects of the same class
    # if a_object == b_object return True
    # Need to find where artist objects are compared to see it in action. 
    # Just saw above that it's done in the TESTS!
    # Because pytest also uses database_connection to connect to the database
    # in it's own test environment. 
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
