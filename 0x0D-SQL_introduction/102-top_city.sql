-- Display the top 3 cities with the highest temperaturse during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 'July' OR month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
