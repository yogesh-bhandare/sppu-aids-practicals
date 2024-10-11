CREATE DATABASE flaskdb;

USE flaskdb;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

SELECT * FROM users;

DROP TABLE users;