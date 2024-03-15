-- SQL script to create table with a unique id
-- Create the table with a unique_id.
CREATE TABLE IF NOT EXISTS `unique_id` (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
