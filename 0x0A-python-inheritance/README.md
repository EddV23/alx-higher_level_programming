# 0x0A. Python - Inheritance

# Python Inheritance Project

## Overview

This project focuses on the concept of inheritance in Python. It covers various tasks that involve creating classes, implementing inheritance, and understanding the usage of built-in functions related to inheritance.

---

## Learning Objectives

By completing this project, you will be able to:

- Explain the concept of inheritance in Python
- Define and use superclass, base class, and subclass
- List attributes and methods of a class or instance
- Inherit a class from another
- Implement multiple inheritance
- Override methods or attributes inherited from the base class
- Understand the purpose of inheritance in Python
- Use built-in functions like `isinstance`, `issubclass`, `type`, and `super`

---

## Project Structure

The project is organized into tasks, each addressing specific aspects of Python inheritance. The tasks include creating classes, implementing methods, and handling error cases.

---

### Tasks

1. **Lookup Function**
**[0-lookup.py](0-lookup.py)**: Write a function to return the list of available attributes and methods of an object.

2. **MyList Class**
**[1-my_list.py](1-my_list.py)**: Create a class `MyList` that inherits from the built-in `list` class. Implement a method to print the sorted list.

3. **is_same_class Function**
**[2-is_same_class.py](2-is_same_class.py)**: Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise, `False`.

4. **is_kind_of_class Function**
**[3-is_kind_of_class.py](3-is_kind_of_class.py)**: Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, `False`.

5. **inherits_from Function**
**[4-inherits_from.py](4-inherits_from.py)**: Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, `False`.

6. **BaseGeometry Class**
 **[5-base_geometry.py](5-base_geometry.py)**: Implement an empty class `BaseGeometry`.

7. **Improved BaseGeometry**
**[6-base_geometry.py](6-base_geometry.py)**: Enhance the `BaseGeometry` class by adding a method `area` that raises an exception.

8. **Rectangle Class**
**[7-base_geometry.py](7-base_geometry.py)**: Create a class `Rectangle` that inherits from `BaseGeometry`. Implement instantiation with width and height.

9. **Full Rectangle Class**
**[8-rectangle.py](8-rectangle.py)**: Extend the `Rectangle` class to include the implementation of the `area` method. Improve the string representation.

10. **Square Class #1**
**[9-rectangle.py](9-rectangle.py)**: Create a class `Square` that inherits from `Rectangle`. Implement instantiation with size.

11. **Square Class #2**
**[10-square.py](10-square.py)**: Extend the `Square` class to improve the string representation.

12. **MyInt Class**
**[100-my_int.py](100-my_int.py)**: Write a class `MyInt` that inherits from `int` and has inverted `==` and `!=` operators.

13. **add_attribute Function**
**[101-add_attribute.py](101-add_attribute.py)**: Write a function that adds a new attribute to an object if it’s possible. Raise a `TypeError` exception if the object can’t have a new attribute.

---

### Requirements

- Python Scripts: Use allowed editors (vi, vim, emacs), Python 3.8.5, and follow coding style using pycodestyle.
- Python Test Cases: Use allowed editors, write test files in the `tests` directory, and ensure proper documentation.
- Documentation: Include README.md, module, class, and function documentation using proper sentences.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/alx-higher_level_programming.git
cd alx-higher_level_programming/0x0A-python-inheritance
```

2. Execute the Python scripts:

```bash
./0-main.py
./1-main.py
# ... (execute other main files as needed)
```

3. Run the test cases:

```bash
python3 -m doctest ./tests/*
```

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.