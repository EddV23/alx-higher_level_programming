# 0x14. Javascript - Web scraping

## Learning Objectives
### General
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

## More Info
### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
Documentation
```bash
$ sudo npm install semistandard --global
```

### Install request module and use it
Documentation
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).


## Tasks

* **0. Readme**
  * [0-readme.js](./0-readme.js): JavaScript script that reads and prints the
  contents of a file.
  * Usage: `./0-readme.js <file path>`.

* **1. Write me**
  * [1-writeme.js](./1-writeme.js): JavaScript script that writes a string to a
  file.
  * Usage: `./1-writeme.js <file path> <string to write>`.

* **2. Status code**
  * [2-statuscode.js](./2-statuscode.js): JavaScript script that displays the
  stauts code of a `GET` request using the `request` framework.
  * Usage: `./2-statuscode.js <URL to GET>`.
  * Output: `code: <status code>`.

* **3. Star wars movie title**
  * [3-starwars_title.js](./3-starwars_title.js): JavaScript script that uses the
  Star Wars API to print the title of the Star Wars movie with a given integer episode
  number.
  * Usage: `./3-starwars_title.js <3-starwars_title.js>`.

* **4. Star wars Wedge Antilles**
  * [4-starwars_count.js](./4-starwars_count.js): JavaScript script that uses the
  Star Wars API to print the number of movies featuring the character "Wedge Antilles".
  * Usage: `./4-starwars_count.js http://swapi.co/api/films/`.

* **5. Loripsum**
  * [5-request_store.js](./5-request_store.js): JavaScript script that stores the
  contents of a webpage in a file.
  * Usage: `./5-request_store.js <URL to get> <file path to store content in>`.

* **6. How many completed?**
  * [6-completed_tasks.js](./6-completed_tasks.js): JavaScript script that uses the
  JSONPlaceholder API to compute the number of tasks completed per user ID.
  * Usage: `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`.

* **7. Who was playing in this movie?**
  * [100-starwars_characters.js](./100-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie.
  * Usage: `./100-starwars_characters.js <movie ID>`.

* **8. Right order**
  * [101-starwars_characters.js](./101-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie in
  the same order as they are listed in the `characters` list of the `/films/` response.
  * Usage: `./101-starwars_characters.js <movie ID>`.

* **9. Twitter Auth**
  * [102-search_twitter.js](./102-search_twitter.js): JavaScript script that sends
  a search request to the Twitter API with a given search string.
  * Usage: `./102-search_twitter.js <consumer  key> <consumer secret> <search string>.
  * Outputs 5 results in the format `[<Tweet ID>] <Tweet text> by <Tweet owner name>`.
