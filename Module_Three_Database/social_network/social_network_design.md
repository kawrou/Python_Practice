# social network two tables recipe:

<!-- 1. Extract nouns from the user stories or specification -->
# User Story:
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

# Nouns:

email address, username, posts, title, content, views

TABLE 1: User
email address, username

TABLE 2: Posts
title, content, views


<!-- 2. Infer the Table Name and Columns -->

---------------------------------------------
|Record  | properties                        |
---------------------------------------------
|User | email_address, username              |
---------------------------------------------
|Posts  | title, content, views              |
---------------------------------------------


Table 1 name: users
Column names: email_address, username

Table 2 name: posts
Columns names: title, content, views

<!-- 3. Decide the column types -->

Table 1: users
id: SERIAL
email_address: text
username: text

Table 2: posts
id: SERIAL
title: text
content: text
views: int
user_id: int

<!-- 5. Relationship -->
users have many posts
Therefore, the foreign key is on the posts table. 

<!-- 5. Write the SQL -->

-- file: students_table.sql

CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    email_address text, 
    username text, 
)

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text, 
  views int,
  constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
);

<!-- 5. Create the table -->

`psql -h 127.0.0.1 recipes_directory < recipes.sql`

<!-- (1) make sure to run an INSERT query to insert a new movie record, -->

INSERT INTO users (email_address, username) VALUES ('aisha@hotmail.com', 'aisha');

INSERT INTO posts (title, content, views, user_id) VALUES ('I'm feeling great', 'It's been a great day', 500, 1);

<!-- (2) and then a SELECT query to list the records. -->
# table 1
SELECT * FROM users;
SELECT username FROM users WHERE id = 1;

# table 2
SELECT * FROM posys;
SELECT title FROM posts WHERE id = 1;