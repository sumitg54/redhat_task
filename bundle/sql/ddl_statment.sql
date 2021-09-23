
--Create the DB if not exists in MYSQL
CREATE DATABASE if not exists comic_db;

--Create the DB if not exists in MYSQL
CREATE TABLE if not exists comic_db.comic (
comic_name VARCHAR(255), 
alt_text VARCHAR(255), 
number int, 
link VARCHAR(255),
image VARCHAR(255), 
imageLink VARCHAR(255)
);

--Truncate table if requried
TRUNCATE TABLE comic_db.comic;