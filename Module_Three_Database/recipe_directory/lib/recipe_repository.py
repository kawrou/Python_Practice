from lib.recipe import Recipe


class RecipeRepository:
    def __init__(self, conection):
        self._conection = conection

    def all(self):
        recipes = self._conection.execute("SELECT * FROM recipes")
        food_list = []
        for row in recipes:
            obj = Recipe(row["id"], row["name"], row["average_cooking_time"], row["rating"])
            food_list.append(obj)
        return food_list

    def find(self, id):
        recipes = self._conection.execute(
            'SELECT * from recipes WHERE id = %s', [id])
        recipe = recipes[0]
        return Recipe(recipe["id"], recipe["name"], recipe["average_cooking_time"], recipe["rating"])

