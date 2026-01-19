CREATE DATABASE IF NOT EXISTS instagram;
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

INSERT INTO users
VALUES
(01,19, "Shreyash","shreyashsature@gmai.com",719,720);

SELECT * FROM users;
DROP TABLE users;