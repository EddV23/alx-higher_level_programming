-- Display the top 3 cities' temperature during July and August ordered by tempe
-- rature (descending)
SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
