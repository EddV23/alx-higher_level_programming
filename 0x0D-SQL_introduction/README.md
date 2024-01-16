# SQL Introduction Project

This project covers various SQL tasks related to MySQL databases.

## General Information

### What's a Database?
A database is a structured collection of data that is organized to be easily accessed, managed, and updated.

### What's a Relational Database?
A relational database is a type of database that uses a structure that allows us to identify and access data in relation to another piece of data in the database.

### What Does SQL Stand For?
SQL stands for Structured Query Language. It is a standard language for interacting with relational databases.

### What's MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web applications and is an essential part of the LAMP stack.

## How to Use

### Requirements
- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)
- Allowed editors: vi, vim, emacs

### Installation
To install MySQL 8.0 on Ubuntu 20.04 LTS, use the following commands:
```bash
$ sudo apt update
$ sudo apt install mysql-server
```

### Connecting to MySQL Server
```bash
$ sudo mysql
```

#Container on Demand
For running MySQL in a container, use the provided credentials:

- Username: root
- Password: root

### Examples
- To list all databases:

```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

## Project Structure
- . [**List Databases**](0x0D-SQL_introduction/0-list_databases.sql): Display all databases on the MySQL server.

- . [**Create Database If Missing**](0x0D-SQL_introduction/1-create_database_if_missing.sql): Create the `hbtn_0c_0` database if it doesn't exist.

- . [**Delete Database**](0x0D-SQL_introduction/2-remove_database.sql): Delete the `hbtn_0c_0` database if it exists.

- . [**List Tables**](0x0D-SQL_introduction/3-list_tables.sql): List all tables in a specified database.

- . [**Create First Table**](0x0D-SQL_introduction/4-first_table.sql): Create the `first_table` if it doesn't exist.

- . [**Full Table Description**](0x0D-SQL_introduction/5-full_table.sql): Print the full description of the `first_table`.

- . [**List All in Table**](0x0D-SQL_introduction/6-list_values.sql): List all rows in the `first_table`.

- . [**Insert New Row**](0x0D-SQL_introduction/7-insert_value.sql): Insert a new row into the `first_table`.

- . [**Count Records with ID 89**](0x0D-SQL_introduction/8-count_89.sql): Display the number of records with `id = 89` in the `first_table`.

- . [**Full Table Creation**](0x0D-SQL_introduction/9-full_creation.sql): Create the `second_table` and add multiple rows.

- . [**List by Best Score**](0x0D-SQL_introduction/10-top_score.sql): List all records of the `second_table` ordered by score.

- . [**Select Best Score**](0x0D-SQL_introduction/11-best_score.sql): List records with a score >= 10 in the `second_table` ordered by score.

- . [**No Cheating**](0x0D-SQL_introduction/12-no_cheating.sql): Update the score of Bob to 10 in the `second_table` using only the name.

- . [**Score Too Low**](0x0D-SQL_introduction/13-change_class.sql): Remove records with a score <= 5 from the `second_table`.

- . [**Average**](0x0D-SQL_introduction/14-average.sql): Compute the score average of all records in the `second_table`.

- . [**Number by Score**](0x0D-SQL_introduction/15-groups.sql): List the number of records with the same score in the `second_table`.

- . [**Say My Name**](0x0D-SQL_introduction/16-no_link.sql): List all records of the `second_table` without rows with an empty name.

- . [**Go to UTF8**](0x0D-SQL_introduction/100-move_to_utf8.sql): Convert the `hbtn_0c_0` database and `first_table` to UTF8.

- . [**Temperatures #0**](0x0D-SQL_introduction/101-avg_temperatures.sql): Display the average temperature by city ordered by temperature (descending).

- . [**Temperatures #1**](0x0D-SQL_introduction/102-top_city.sql): Display the top 3 cities' temperature during July and August ordered by temperature (descending).

- . [**Temperatures #2**](0x0D-SQL_introduction/103-max_state.sql): Display the max temperature of each state ordered by state name.

