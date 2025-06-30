Calculator Module
-----------------

Overview
--------
The Calculator module is a Python project that implements a Calculator class for basic arithmetic operations. 
The Calculator class keeps track of its current memory value, which is updated each time an operation is performed.
It can perform:
- Addition / Subtraction
- Multiplication / Division
- nth Root (using a user-specified degree)
- Memory Reset (resets the memory to 0)

Installation
------------
1. Download or copy the project files to your local desktop.
2. Ensure you have Python installed on your system.
3. To run unit tests, install pytest by running:
   
       pip install pytest

Structure
-----------------
Project includes the following files:
- calculator.py: contains the Calculator class and its methods.
- test_calculator.py: contains unit tests for the Calculator class.
- calculator_demo.py: a demo script that shows how to use the Calculator class.
- calculatordemo.ipynb: a demo in Jupyter notebook.
- README.txt: file, which provides an overview and instructions of the project.

Usage
-----
To use the Calculator module in your own project, import the Calculator class from `calculator.py`. Example:

    from calculator import Calculator

    # Create a new Calculator instance
    variable = Calculator()

    # Set an operator and perform an operation
    variable.check_operator("+")
    variable.perform_operation(5)   # This will add 5 to the memory
    print(variable)                 # Displays the current result

The Calculator class includes the following methods:
- add(number): adds the given number to the memory value.
- sub(number): subtracts the given number from the memory value.
- mult(number): multiplies the memory value by the given number.
- div(number): divides the memory value by the given number. Raises a ZeroDivisionError if the number is 0.
- nth_root(number): calculates the nth root of the memory value (where n is provided by the user). Raises a ZeroDivisionError if n is 0.
- reset(): resets the memory to 0 and clears the operator.
- check_operator(operator): validates and sets the operator. Raises a ValueError if an invalid operator is given.
- perform_operation(number=0): executes the operation based on the operator and the given number. Uses default value of 0 for operations that don't require an additional number.

Demo
----
A demonstration of how to use the Calculator class is provided in the `calculator_demo.py` file. To run the demo, execute:

    python calculator_demo.py

The demo will prompt you to choose an operation and provide a number. It will then perform the calculation and show the current result. Enter 'finish' to end the demo session.

Also you can use 'calculatordemo.ipynb' file for demo in the Jupyter Notebook environment. It provides step-by-step code cells and outputs to demonstrate how the Calculator module works.
Open this notebook using Jupyter Notebook or VS Code's Jupyter extension.

Testing
-------
Unit tests are provided in the `test_calculator.py` file. To run the tests, use pytest with the following command:

    pytest test_calculator.py

These tests ensure that:
- All arithmetic operations (addition, subtraction, multiplication, division, nth_root) work correctly.
- The reset operations updates the memory as expected.
- The string representation (__str__) of the Calculator class displays the correct format.
- Appropriate errors are raised when invalid operations or inputs are provided.
