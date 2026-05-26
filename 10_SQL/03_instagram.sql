CREATE DATABASE instagram;
USE instagram;

CREATE TABLE users
(id INT PRIMARY KEY,
name VARCHAR(15) NOT NULL,
email VARCHAR(30) UNIQUE,
followers INT DEFAULT 0,
age INT,
following INT, 
CONSTRAINT age_check CHECK (age >=13)
);


INSERT INTO users
(id , name, email, followers, age, following)
VALUES
(1, "shreyash", "shreyashsature@gmail.com", 11, 21,20),
(2, "shreya", "shreya@gmail.com", 13, 21, 22),
(3, "shrey", "shsature@gmail.com", 18, 21, 22),
(4, "yash", "shreysature@gmail.com", 81, 21, 65),
(5, "shreyya", "shreesature@gmail.com", 65, 21, 54);

CREATE TABLE posts
(id INT PRIMARY KEY, 
post VARCHAR(20) , 
user_id INT, 
FOREIGN KEY (user_id) REFERENCES users(id)
);
