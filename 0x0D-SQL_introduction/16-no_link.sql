-- List all records of the second_table without rows with empty name
SELECT * FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
