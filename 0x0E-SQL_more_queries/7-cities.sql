-- SQL script to create a databaseand with an auto incremented ID in a table
-- Create database hbtn_0 with the table cities and an auto incremented ID
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY(`id`),
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
