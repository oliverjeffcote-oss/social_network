-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255)
);

-- CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    contents VARCHAR(255),
    views INTEGER,
    account_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run

-- Accounts
INSERT INTO accounts (email_address, username) VALUES ('elliot.smith@example.com', 'ElliotS');
INSERT INTO accounts (email_address, username) VALUES ('joan.baez@example.com', 'JoanB');
INSERT INTO accounts (email_address, username) VALUES ('kendrick.lamar@example.com', 'KDot');
INSERT INTO accounts (email_address, username) VALUES ('daft.punk@example.com', 'DPunk');

-- Posts
INSERT INTO posts (title, contents, views, account_id) VALUES ('Between the Bars', 'Short and sweet.', 152, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('Waltz #2', 'Melancholy melody.', 98, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('Diamonds & Rust', 'A memory in music.', 201, 2);
INSERT INTO posts (title, contents, views, account_id) VALUES ('Gracias a la Vida', 'A cover of hope.', 134, 2);
INSERT INTO posts (title, contents, views, account_id) VALUES ('Alright', 'We gon be alright.', 542, 3);
INSERT INTO posts (title, contents, views, account_id) VALUES ('HUMBLE.', 'Sit down.', 678, 3);
INSERT INTO posts (title, contents, views, account_id) VALUES ('One More Time', 'Celebrate and dance.', 430, 4);
INSERT INTO posts (title, contents, views, account_id) VALUES ('Instant Crush', 'Love in disguise.', 319, 4);
