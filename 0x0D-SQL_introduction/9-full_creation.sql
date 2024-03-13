-- SQL script that creates another table in a database
-- Create another table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
) VALUES ( (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8) );
