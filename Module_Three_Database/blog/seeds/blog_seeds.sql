DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  name text,
  content text, 
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_artist foreign key(post_id)
    references posts(id)
    on delete cascade
);


INSERT INTO posts(title, content) VALUES 
  ('The Art of Coding', 'Exploring the beauty and creativity in programming'),
  ('Machine Learning Trends', 'Exploring the latest developments in machine learning'),
  ('Healthy Cooking Tips', 'Nutritious recipes and cooking hacks for a healthier lifestyle'),
  ('Traveling on a Budget', 'Discovering amazing destinations without breaking the bank'),
  ('The World of Literature', 'Diving into classic and contemporary works of literature');


INSERT INTO comments(name, content, post_id) 
VALUES 
  ('John Doe', 'Great post! I learned a lot.', 1),
  ('Alice Smith', 'This is fascinating. Can`t wait for more!', 2),
  ('Bob Johnson', 'Thanks for the tips. Trying the recipe tonight!', 3),
  ('Eva Rodriguez', 'Your travel stories inspire me to explore!', 4),
  ('Sarah Brown', 'I appreciate your insights. Keep up the good work!', 5);