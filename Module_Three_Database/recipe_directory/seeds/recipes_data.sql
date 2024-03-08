-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS Recipes;
DROP SEQUENCE IF EXISTS Recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS Recipes_id_seq;
CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    average_cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO Recipes (name, average_cooking_time, rating) VALUES 
    ('Spaghetti Bolognese', 30, 4.8),
    ('Chicken Alfredo', 40, 4.6), 
    ('Chocolate Cake', 60, 4.9),
    ('Caesar Salad', 15, 4.3),
    ('Margherita Pizza', 25, 4.7),
    ('Grilled Salmon', 35, 4.5);



