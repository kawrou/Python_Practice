from lib.recipe_repository import *
from lib.recipe import *


def test_all_returns_list_of_recipes(db_connection):
        db_connection.seed("seeds/recipes_data.sql")
        repository = RecipeRepository(db_connection)
        recipes = repository.all()

        assert recipes == [
            Recipe(1, 'Spaghetti Bolognese', 30, 5),
            Recipe(2, 'Chicken Alfredo', 40, 5), 
            Recipe(3, 'Chocolate Cake', 60, 5),
            Recipe(4, 'Caesar Salad', 15, 4),
            Recipe(5, 'Margherita Pizza', 25, 5),
            Recipe(6, 'Grilled Salmon', 35, 5)
        ]

def test_find_recipe(db_connection):
        db_connection.seed("seeds/recipes_data.sql")
        repository = RecipeRepository(db_connection)
        found_recipe = repository.find(5)

        assert found_recipe == Recipe(5, 'Margherita Pizza', 25, 5)
