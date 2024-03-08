--# social_network.sql

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    email_address VARCHAR(255), 
    username VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INTEGER, 
    user_id int, 
    constraint fk_users foreign key(user_id)
        references users(id)
        on delete cascade
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (email_address, username) VALUES ('aisha@hotmail.com', 'aisha');
INSERT INTO users (email_address, username) VALUES ('john.doe@example.com', 'john_doe');
INSERT INTO users (email_address, username) VALUES ('emma.smith@gmail.com', 'emma_smith');
INSERT INTO users (email_address, username) VALUES ('michael.jones@yahoo.com', 'michael_jones');
INSERT INTO users (email_address, username) VALUES ('laura.miller@hotmail.com', 'laura_miller');
INSERT INTO users (email_address, username) VALUES ('kevin.white@gmail.com', 'kevin_white');
INSERT INTO users (email_address, username) VALUES ('natalie.brown@yahoo.com', 'natalie_brown');
INSERT INTO users (email_address, username) VALUES ('peter.clark@example.com', 'peter_clark');
INSERT INTO users (email_address, username) VALUES ('olivia.wilson@hotmail.com', 'olivia_wilson');
INSERT INTO users (email_address, username) VALUES ('sam.carter@gmail.com', 'sam_carter');


INSERT INTO posts (title, content, views, user_id) VALUES ('I`m feeling great', 'It`s been a great day', 500, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Exploring New Horizons', 'Embarking on a journey of discovery', 320, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Coding Adventures', 'Diving deep into the world of programming', 250, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Nature`s Beauty', 'Capturing the wonders of the great outdoors', 800, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('Bookworm`s Delight', 'A world of imagination within the pages', 420, 5);
INSERT INTO posts (title, content, views, user_id) VALUES ('Fitness Journey', 'Transforming mind and body through fitness', 670, 6);
INSERT INTO posts (title, content, views, user_id) VALUES ('Travel Diaries', 'Wandering through diverse cultures and landscapes', 550, 7);
INSERT INTO posts (title, content, views, user_id) VALUES ('Culinary Adventures', 'Savoring flavors from around the globe', 720, 8);
INSERT INTO posts (title, content, views, user_id) VALUES ('Artistic Expressions', 'Unleashing creativity on canvas', 380, 9);
INSERT INTO posts (title, content, views, user_id) VALUES ('Mindful Living', 'Balancing life with mindfulness practices', 600, 10);
INSERT INTO posts (title, content, views, user_id) VALUES ('Tech Trends', 'Exploring the latest in technology', 550, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Healthy Habits', 'Building a foundation for a healthier lifestyle', 480, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Gaming Chronicles', 'Diving into the virtual realms of gaming', 720, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('DIY Crafts', 'Crafting unique creations from the heart', 380, 5);
INSERT INTO posts (title, content, views, user_id) VALUES ('Movie Buff`s Corner', 'Analyzing the art of cinema', 620, 6);
INSERT INTO posts (title, content, views, user_id) VALUES ('Photography Journey', 'Freezing moments in time through the lens', 540, 7);
INSERT INTO posts (title, content, views, user_id) VALUES ('Business Insights', 'Navigating the complexities of entrepreneurship', 670, 8);
INSERT INTO posts (title, content, views, user_id) VALUES ('Parenting Adventures', 'Guiding the next generation through parenthood', 430, 9);
INSERT INTO posts (title, content, views, user_id) VALUES ('Fashion Forward', 'Exploring trends in the world of fashion', 580, 10);
INSERT INTO posts (title, content, views, user_id) VALUES ('Music Melodies', 'Harmonizing life with the rhythm of music', 490, 1);



