-- SQL script that imports a database and display the average temperatur
-- Import database and display temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
