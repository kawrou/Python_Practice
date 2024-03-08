class Album:
    """A class to hold album data"""
    #Initialize with all attributes
    # Each attributes come from the columns in the tables in the database / SQL file
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    #Checks equality between the returned instances of albums from the database
    #And the original instance of albums
    #Because, even though the values can be the same, they are different instances
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    #A nicely formatted string of the instances
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
