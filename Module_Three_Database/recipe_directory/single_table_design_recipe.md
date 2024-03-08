
### 1. Extract nouns from the user stories or specs

```
# EXAMPLE USER STORY:
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

Nouns: recipes, name, average cooking time, rating

### 2. Infer the Table Name and Columns

|Record|Properties         |
|recipes |name, average cooking time, rating|


Name of the table (always plural): Recipes

Column names: name, average cooking time, rating

### 3. Decide the column types

text, int, bigint, numeric, boolean
VARCHAR, CHAR, FLOAT, 

**ALWAYS** have the primary key ==id== as a first column. It's type will always be SERIAL

```
# EXAMPLE:

id: SERIAL
name: text
average cooking time: int
rating: int
```

### 4. Write the SQL


```
-- EXAMPLE
-- file: recipe_db.sql

-- Replace the table name, columm names and types.

CREATE TABLE Recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR
  average cooking time INT
  rating INT
);
```

### 5. Create the table

```shell
psql -h 127.0.0.1 recipe_directory < recipe_data.sql
```

SO YOU SHOULD CREATE THE SQL FILE AS THE SEED FOR THE DATABASE


#design_recipe
