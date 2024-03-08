CREATE TABLE movies(
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_year INT
);


INSERT INTO movies (title, genre, release_year) VALUES 
('The Adventure Begins', 'Action', 2020),
('Mystery Manor', 'Mystery', 2019),
('Love in the City', 'Romance', 2021),
('Sci-Fi Odyssey', 'Science Fiction', 2022),
('Comedy Central', 'Comedy', 2018),
('Drama Junction', 'Drama', 2017),
('Thriller Express', 'Thriller', 2023);
