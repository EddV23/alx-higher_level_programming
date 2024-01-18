# Project 0x0E - SQL: More Queries

## Description

This project focuses on enhancing SQL skills by working on more advanced queries, covering various aspects of database management.

## Learning Objectives
### General
- 1. Create a new MySQL user:
```sql
-- Create a new user 'new_user' with password 'password'
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

- 2. Manage privileges for a user to a database or table:
```sql
-- Grant SELECT and INSERT privileges on 'database_name' to 'new_user'
GRANT SELECT, INSERT ON database_name.* TO 'new_user'@'localhost';

-- Grant ALL privileges on 'table_name' to 'new_user'
GRANT ALL ON database_name.table_name TO 'new_user'@'localhost';
```

- 3. PRIMARY KEY:
-- A PRIMARY KEY is a unique identifier for a record in a table.
-- It must contain unique values, and it cannot contain NULL values.

- 4. FOREIGN KEY:
-- A FOREIGN KEY is a field that refers to the PRIMARY KEY in another table.

- 5. NOT NULL and UNIQUE constraints:
```sql
-- Create a table 'example_table' with a NOT NULL and UNIQUE constraint
CREATE TABLE example_table (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    other_column INT
);
```

- 6. Retrieve data from multiple tables in one request:
```sql
-- Select data from 'table1' and 'table2' based on a common column 'id'
SELECT * FROM table1
JOIN table2 ON table1.id = table2.id;
```

- 7. Subqueries:
```sql
-- Select students from 'students' table who have a GPA greater than the average GPA
SELECT id, name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);
```

- 8. JOIN:
-- Combines rows from two or more tables based on a related column between them.

- 9. UNION:
-- Combines the result sets of two or more SELECT statements.


## Requirements
### File Structure:
- All files should have a new line at the end.
- All SQL queries should be in uppercase (e.g., SELECT, WHERE).
- Each file should start with a comment describing the task.
- Use allowed editors: vi, vim, emacs.

### README.md:
- A README.md file at the root with project information.

### SQL Execution:
- All SQL files will be executed on Ubuntu 20.04 LTS using MySQL 8.0.25.

### Comments:
- Include comments for SQL files to explain the purpose of each query.

### MySQL Installation:
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

### Connect to MySQL:
```bash
$ sudo mysql
```

### Container-on-Demand:
- Credentials in the container are root/root.

### Import SQL Dump:
- Example of importing a SQL dump:
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```
- Password prompt will appear.
Note: Ensure MySQL is started in the container before executing queries.


## Files and Descriptions

1. [**`0-privileges.sql`**](./0-privileges.sql): SQL script that sets up privileges for the `hbtn_0e_0_usa` user.

2. [**`1-create_user.sql`**](./1-create_user.sql): SQL script that creates a new user in the database.

3. [**`2-create_read_user.sql`**](./2-create_read_user.sql): SQL script that creates a new user with specific privileges.

4. [**`3-force_name.sql`**](./3-force_name.sql): SQL script that updates a user's name in the database.

5. [**`4-never_empty.sql`**](./4-never_empty.sql): SQL script that updates a user's biography and ensures it is never empty.

6. [**`5-unique_id.sql`**](./5-unique_id.sql): SQL script that adds a unique constraint to the `id` field of the `users` table.

7. [**`6-states.sql`**](./6-states.sql): SQL script that creates a new table and populates it with data.

8. [**`7-cities.sql`**](./7-cities.sql): SQL script that creates a new table linked to the `states` table.

9. [**`8-cities_of_california_subquery.sql`**](./8-cities_of_california_subquery.sql): SQL script that lists all the cities in California using a subquery.

10. [**`9-cities_by_state_join.sql`**](./9-cities_by_state_join.sql): SQL script that lists all cities with their corresponding state using a join.

11. [**`10-genre_id_by_show.sql`**](./10-genre_id_by_show.sql): SQL script that lists TV show names with their associated genre.

12. [**`11-genre_id_all_shows.sql`**](./11-genre_id_all_shows.sql): SQL script that lists all genres with the names of the shows they are associated with.

13. [**`12-no_genre.sql`**](./12-no_genre.sql): SQL script that lists shows with no associated genre.

14. [**`13-count_shows_by_genre.sql`**](./13-count_shows_by_genre.sql): SQL script that counts the number of shows for each genre.

15. [**`14-my_genres.sql`**](./14-my_genres.sql): SQL script that lists all genres of a specific user.

16. [**`15-comedy_only.sql`**](./15-comedy_only.sql): SQL script that lists only comedy shows.

17. [**`16-shows_by_genre.sql`**](./16-shows_by_genre.sql): SQL script that lists shows with their respective genres.

18. [**`100-not_my_genres.sql`**](./100-not_my_genres.sql): SQL script that lists genres not associated with a specific user.

19. [**`101-not_comedy.sql`**](./101-not_comedy.sql): SQL script that lists shows not categorized as comedy.

20. [**`102-rating_shows.sql`**](./102-rating_shows.sql): SQL script that updates the rating of a TV show.

## Examples

1. Run the SQL scripts using the MySQL command-line tool:

    ```bash
    mysql -hlocalhost -uroot -p hbtn_0e_0_usa < 0-privileges.sql
    ```

2. Verify the changes in the MySQL console:

    ```sql
    SELECT * FROM users;
    ```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
