DROP TABLE IF EXISTS housing.user;
DROP SCHEMA IF EXISTS housing;
CREATE SCHEMA housing;
CREATE TABLE housing.user (
    id INT,
    name VARCHAR(50),
    price INT
);