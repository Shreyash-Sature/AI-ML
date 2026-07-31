-- WHERE clause
/*

Synatx :

SELECT column1, column2
FROM table
WHERE conditions

*/
/*

SELECT command  : Used to print or display columns.

Synatx:

SELECT column1, column2     (displays selected columns)
FROM table_name;

SELECT * FROM table_name;   (displays all columns)
*/

USE instagram;

SELECT name
FROM users
WHERE age>20 AND followers>25;

select * from users;

