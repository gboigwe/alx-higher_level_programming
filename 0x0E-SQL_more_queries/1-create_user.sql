-- SQL script to create MySQL server user for user_0d_1
-- Create a user for user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
