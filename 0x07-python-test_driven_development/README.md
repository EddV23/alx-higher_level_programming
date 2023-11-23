Project Title
0x07. Python Test-Driven Development

Overview

This repository contains a collection of Python scripts developed following the principles of test-driven development (TDD). The scripts cover various topics, including integers addition, matrix operations, string processing, and more.



Table of Contents

Project Structure
Requirements
Usage
Tests
Contributing
License



Project Structure
The project is organized into directories, each addressing a specific topic. The directories include:

0x07-python-test_driven_development: Main project directory.
0-add_integer.py: Function for adding two integers.
tests/0-add_integer.txt: Test cases for 0-add_integer.py.
2-matrix_divided.py: Function for dividing all elements of a matrix.
tests/2-matrix_divided.txt: Test cases for 2-matrix_divided.py.
3-say_my_name.py: Function for printing a name.
tests/3-say_my_name.txt: Test cases for 3-say_my_name.py.
4-print_square.py: Function for printing a square of '#'.
tests/4-print_square.txt: Test cases for 4-print_square.py.
5-text_indentation.py: Function for printing text with indentation.
tests/5-text_indentation.txt: Test cases for 5-text_indentation.py.
6-max_integer.py: Function for finding the max integer in a list.
tests/6-max_integer_test.py: Unittests for 6-max_integer.py.
100-matrix_mul.py: Function for matrix multiplication.
tests/100-matrix_mul.txt: Test cases for 100-matrix_mul.py.
101-lazy_matrix_mul.py: Function for lazy matrix multiplication using NumPy.
tests/101-lazy_matrix_mul.txt: Test cases for 101-lazy_matrix_mul.py.
102-python.c: C implementation for printing Python string information.
tests/102-tests.py: Test cases for 102-python.c.



Requirements

Python 3.4
NumPy (for 101-lazy_matrix_mul.py)



Usage

To run the scripts or tests, use the following commands:
# Run a specific script
python3 0-add_integer.py

# Run doctests for a script
python3 -m doctest -v ./tests/0-add_integer.txt

# Compile and run C code
gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
python3 102-tests.py



Tests

The project includes tests for each script, located in the respective tests directories. To run all tests, execute the following:

python3 -m unittest discover tests



Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.



License

This project is licensed under the MIT License.