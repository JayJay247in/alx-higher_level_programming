# 0x07. Python - Test-driven development

An introductory project into creating doctests and unittests

## Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)

- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)

- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## File Descriptions

| Filename                      | Description                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
|             | Function that adds two integers (Doctest on )                                                        |
|          | Function that divides all elemtns of a matrix (Doctest on )                                       |
|             | Function that prints  (Doctest on )                             |
|            | Function that prints a square with the character  (Doctest on )                                  |
|        | Function that prints a text with 2 new lines after each of these ,  and  (Doctest on ) |
|  | Unittests for the function                                                                          |
|            | Function that multiplies 2 matrices (Doctest on )                                                   |
|       | Function that multiplies 2 matrices by using the module NumPy (Doctest on )                    |
|                 | Function that prints Python strings                                                                                           |

## Tasks

- **0. Integers addition**

  - [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
    of two numbers.
  - If either of  or  is not an  or , a  is raised
    with the message  or .
  - If either of  or  is a , it is casted to an 
    before addition.

- **1. Divide a matrix**

  - [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
    elements of a matrix by a common divisor.
  - Returns a new matrix representing the division of all elements of 
    by .
  - Quotients are rounded to two decimal places.
  - If  is not a list of lists of s or s, a 
    is raised with the message .
  - If  contains rows of different lengths, a  is raised
    with the message .
  - If the divisor  is not an  or , a  is raised
    with the message .
  - If  is , a  is raised with the message
    .

- **2. Say my name**

  - [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
    the format .
  - If either of  or  is not a , a  is
    raised with the message  or .

- **3. Print square**

  - [4-print_square.py](./4-print_square.py): Python function that prints a square using
    the  character.
  - The paramter  represents the height/width of the square.
  - If  is not an , a  is raised with the message,
    .
  - If  is less than , a  is raised with the message .

- **4. Text indentation**

  - [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
    indentation.
  - Two new lines are printed after any , , or  character.
  - If  is not a , a  is raised with the message .
  - No spaces are printed at the beginning or end of each printed line.

- **5. Max integer - Unittest**

  - [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script
    that runs unittests for the function 
    (provided by Holberton School).

- **6. Matrix multiplication**

  - [100-matrix_mul.py](./100-matrix_mul.py): Python function that multiplies two matrices.
  - Returns a new matrix representing the multiplication of  by .
  - If either of  or  is empty (ie.  or ), a
     is raised with the message  or .
  - If either of  or  is not a list, a  is raised with
    the message  or  must be a list.
  - If either of  or  is not a list of lists, a  is raised
    with the message  or .
  - If either of  or  is not a list of lists of s or s, a
     is raised with the message  or .
  - If either of  or  contains rows of different lengths, a 
    is raised with the message  or
    .
  - If  and  cannot be multiplied (ie. row size of  does not match
    column size of ), a  is raised with the message .

- **7. Lazy matrix multiplication**

  - [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Python function that multiplies
    two matrices using the module .
  - Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).

- **8. CPython #3: Python Strings**
  - [102-python.c](./102-python.c): C function that prints basic information about Python
    string objects.
