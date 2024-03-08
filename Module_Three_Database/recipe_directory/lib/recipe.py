class Recipe:
    def __init__(self, id, recipe, cooking_time, rating):
        self.id = id
        self.recipe = recipe
        self.cooking_time = cooking_time
        self.rating = rating
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # def __repr__(self):
    #     return f"Recipes({self.id}, {self.recipe}, {self.cooking_time}, {self.rating})"