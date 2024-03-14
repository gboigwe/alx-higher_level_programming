-- SQL script that lists the number of records with same score
-- List all record with same score
SELECT score, COUNT(*) AS num FROM second_table
GROUP BY score
ORDER BY num DESC;
