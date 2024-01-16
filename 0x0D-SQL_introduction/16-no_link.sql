-- List all records of the second_table without rows with empty name
USE hbtn_0c_0;
SELECT * FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
