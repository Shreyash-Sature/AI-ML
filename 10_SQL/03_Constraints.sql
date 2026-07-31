-- CONSTRAINTS : Rules for data in table

-- 01. NOT NULL  (columns cannot have null values)
-- 02. UNIQUE    (all values in column are different)
-- 03. DEFAULT   (sets a default value of column)
-- 04 CHECK      (it can limit values allowed in a column) 

CREATE TABLE users
(id INT PRIMARY KEY,
name VARCHAR(15) NOT NULL,
email VARCHAR(30) UNIQUE,
followers INT DEFAULT 0,
age INT,
following INT, 
CONSTRAINT age_check CHECK (age >=13)
);
