-- SQL script that list all records of the table without excluding row name
-- List records of table and do not exclude row with name
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
