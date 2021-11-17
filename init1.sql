CREATE DATABASE glints_db;
\c glints_db
CREATE TABLE sales
(
	id INTEGER, 
	creation_date TIMESTAMP,
	sale_value INTEGER
);