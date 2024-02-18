# 0x0F. Python - Object-relational mapping

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```bash
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
print(row)
cur.close()
conn.close()
```

With an ORM:
```bash
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Learning Objectives
### General
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## More Info

### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```
Also, you can have this warning message:
```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```
You can ignore it.



## Tests :heavy_check_mark:

* [tests](./tests): SQL and Python scripts used for test tables for the files.

## Tasks :page_with_curl:

* **0. Get all states**
  * [0-select_states.py](./0-select_states.py): Python script that uses MySQLdb
  to list all states in the database `hbtn_0e_0_usa`.
  * Usage: `./0-select_states.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.

* **1. Filter states**
  * [1-filter_states.py](./1-filter_states.py): Python script that uses MySQLdb
  to list all states with names starting with `N` in the database `hbtn_0e_0_usa`.
  * Usage: `./1-filter_states.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.

* **2. Filter states by user input**
  * [2-my_filter_states.py](./2-my_filter_states.py): Python script that uses
  MySQLdb to display all values matching a given name in the `states` table of
  the database `hbtn_0e_0_usa`.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.
  * Uses string formatting to construct the SQL query.

* **3. SQL Injection...**
  * [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Python script
  that uses MySQLdb to display all values matching a given name in the `states`
  table of the database `hbtn_0e_0_usa`.
  * Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
  * Results are ordered by ascending `states.id`.
  * Safe from SQL injections.

* **4. Cities by states**
  * [4-cities_by_state.py](./4-cities_by_state.py): Python script that uses
  MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
  * Usage: `./4-cities_by_state.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `cities.id`.

* **5. All cities by state**
  * [5-filter_cities.py](./5-filter_cities.py): Python script that uses MySQLdb
  to list all cities of a given state in the database `hbtn_0e_4_usa`.
  * Usage: `./5-filter_cities.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `cities.id`.

* **6. First state model**
  * [model_state.py](./model_state.py): Python module defining a class `State`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

* **7. All states via SQLAlchemy**
  * [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): Python script
  that uses SQLAlchemy to list all `State` objects from the database
  `hbtn_0e_6_usa`.
  * Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `states.id`.

* **8. First state**
  * [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): Python script
  that uses SQLAlchemy to print the first `State` object from the database
  `hbtn_0e_6_usa`, ordered by `states.id`.
  * Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password>
  <database name>`.
  * If the `states` table is empty, prints `Nothing`.

* **9. Contains `a`**
  * [9-model_state_filter_a.py](./9-model_state_filter_a.py): Python script
  that uses SQLAlchemy to list all `State` objects that contain the letter `a`
  in the database `hbtn_0e_6_usa`.
  * Usage: `./9-model_state_filter_a.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `states.id`.

* **10. Get a state**
  * [10-model_state_my_get.py](./10-model_state_my_get.py): Python script that
  uses SQLAlchemy to print the `id` of the `State` object with name matching that
  passed as argument in the database `hbtn_0e_6_usa`.
  * Usage: `./10-model_state_my_get.py <mysql username> <mysql password>
  <database name> <state searched name>`.
  * Displays the `id` of the matched `State`.
  * If no match is found, prints `Not found`.

* **11. Add a new state**
  * [11-model_state_insert.py](./11-model_state_insert.py): Python script that
  uses SQLAlchemy to add the `State` object "Louisiana" to the database
`hbtn_0e_6_usa`.
  * Usage: `./11-model_state_insert.py <mysql username> <mysql password>
  <database name>`.
  * Prints the `id` of the new `State` after creation.

* **12. Update a state**
  * [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): Python
  script that uses SQLAlchemy to change the name of the `State` object with
  `id = 2` in the database `hbtn_0e_6_usa` to "New Mexico".
  * Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password>
  <database name>`.

* **13. Delete states**
  * [13-model_state_delete_a.py](./13-model_state_delete_a.py): Python script
  that uses SQLAlchemy to delete all `State` objects with a name containing the
  letter `a` from the database `hbtn_0e_6_usa`.
  * Usage: `./13-model_state_delete_a.py <mysql username> <mysql password>
  <database name>`.

* **14. Cities in state**
  * [model_city.py](./model_city.py): Python module defining a class `City`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.
    * Includes class attribute `state_id` that is a foreign key to
    `states.id`.
  * [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py):
  Python script that uses SQLAlchemy to list all `City` objects in the database
  `hbtn_0e_14_usa`.
  * Usage: `./14-model_city_fetch_by_state.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `cities.id`.

* **15. City relationship**
  * [relationship_state.py](./relationship_state.py): Python module defining a
  class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `states`.
    * Identical to the `State` class defined in [model_state.py](./model_state.py).
    * Includes class attribute `classes` that represents a relationship with
    the class `City`. If the `State` object is deleted, all linked `City` objects
    are also deleted. `State` objects are backreferenced to `City` objects as
    `state`.
  * [relationship_city.py](./relationship_city.py): Python module defining a
  class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `cities`.
    * Identical to the `City` class defined in [model_city.py](./model_city.py).
  * [100-relationship_states_cities.py](./100-relationship_states_cities.py):
  Python script that uses SQLAlchemy to add the `State` "California" with `City`
  "San Francisco" to the database `hbtn_0e_100_usa`.
  * Usage: `./100-relationship_states_cities.py <mysql username>
  <mysql password> <database name>`.
  * Uses the `cities` relationship for all `State` objects.

* **16. List relationship**
  * [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py):
  Python script that uses SQLAlchemy to list all `State` and corresponding
  `City` objects in the database `hbtn_0e_101_usa`.
  * Usage: `./101-relationship_states_cities_list.py <mysql username>
  <mysql password> <database name>`.
  * Uses the `cities` relationship for all `State` objects.
  * Results are sorted by ascending `states.id` and `cities.id`.

* **17. List city**
  * [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py):
  Python script that uses SQLAlchemy to list all `City` objects from the database
  `hbtn_0e_101_usa`.
  * Usage: `./102-relationship_cities_states_list.py <mysql username>
  <mysql password> <database name>`.
  * Uses the `state` relationship to access the `State` objects linked to `City` objects.
  * Results are sorted by ascending `cities.id`.
