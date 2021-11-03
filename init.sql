CREATE DATABASE glints_db;
\c glints_db
CREATE TABLE sales
(
	id INTEGER, 
	creation_date TIMESTAMP,
	sale_value INTEGER
);

INSERT INTO sales
(id, creation_date,sale_value)
VALUES
(0,'2021-10-12',1000)
,(1,'2021-10-13',2000);
