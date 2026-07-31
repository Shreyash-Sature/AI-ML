CREATE DATABASE IF NOT   instagram;
USE instagram;

CREATE TABLE users (
  id INT,
  age INT,
  CONSTRAINT CHECK (age > 13),
  name VARCHAR(30) NOT NULL,
  email VARCHAR(30) UNIQUE,
  following INT DEFAULT 0,
  followers INT
);
/*
INSERT INTO table_name : used to insert data in table

Syntax:

INSERT INTO table_name
(column1, column2, column3)
VALUES
(value1, value2, value3);      ---(maintain  order of values while inserting in column with columns)

*/
INSERT INTO users
VALUES
(01,19, "Shreyash","shreyashsature@gmai.com",719,720)
(02,13, "Shreya","sneha@gmail.com",112, 211);

SELECT * FROM users;
DROP TABLE users;