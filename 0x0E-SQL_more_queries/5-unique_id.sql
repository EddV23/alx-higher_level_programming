-- Step 1: Create the table with a unique constraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) UNIQUE
	);

-- Step 2: Insert the data into the new table, which will only keep unique entries
INSERT IGNORE INTO unique_id (name)
SELECT name FROM unique_id;

-- Step 3: Drop the old table
DROP TABLE unique_id;
