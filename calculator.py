class Calculator:
    """
    Calculator that can do basic math.

    It can add, subtract, multiply, divide numbers, take the nth root,
    and reset its memory. The calculator remembers its current value.
    """

    def __init__(self, memory=0, operator=None):
        """
        Setting up a Calculator.

        Args:
            memory (number): starting value is 0.
            operator (str): set to None at the start.
        """

        self.memory = memory
        self.operator = operator

    def add(self, number):
        self.memory += number
        """
        Adds a number to the memory value.

        Args:
            number (number): the number to add.
        """

    def sub(self, number):
        self.memory -= number
        """
        Substracts a number from the memory value.

        Args:
            number (number): the number to substract.
        """

    def mult(self, number):
        self.memory *= number
        """
        Multiplies the memory value by the number.

        Args:
            number (number): the multiplier.
        """

    def div(self, number):
        """
        Divides the memory value by a number.

        Args:
            number (number): the number to divide by.

        Raises:
            ZeroDivisionError: when the number is 0.
        """

        if number == 0:
            raise ZeroDivisionError("Cannot divide by zero!\n")
        self.memory /= number

    def nth_root(self, number):
        """
        Takes the nth root of the memory value.

        Args:
            number (int): the degree of the root.

        Raises:
            ZeroDivisionError: when the number is 0.
        """
        if number == 0:
            raise ZeroDivisionError("Cannot divide by zero!\n")
        self.memory = self.memory ** (1 / number)

    def reset(self):
        """
        Resets the calculator: sets memory to 0 and clears the operator.
        """
        self.memory = 0
        self.operator = None

    def __str__(self):
        """
        Returns a string showing the memory value.

        If the value is a whole number, shows it as an integer.
        Otherwise, shows it with two decimal places.
        """
        if self.memory % 1 == 0:
            result = f"Current result: {int(self.memory)}"
        else:
            result = f"Current result: {self.memory:.2f}"
        return result

    def check_operator(self, operator):
        """
        Validates the operator and sets it.

        Args:
            operator (str): the operator to validate.

        Raises:
            ValueError: if the operator is not one of the allowed ones.
        """

        valid_operators = {"+", "-", "*", "/", "root", "reset"}
        if operator in valid_operators:
            self.operator = operator
        else:
            raise ValueError(
                "Wrong operator! Choose from: '+', '-', '*', '/', 'root' or 'reset'\n."
            )

    def perform_operation(self, number=0):
        """
        Performs the calculator operation using the given number.

        Args:
            number (number): the number used in the operation, default is 0.

        Raises:
            ValueError: if no operator is set.
        """
        match self.operator:
            case "+":
                self.add(number)
            case "-":
                self.sub(number)
            case "*":
                self.mult(number)
            case "/":
                self.div(number)
            case "root":
                self.nth_root(number)
            case "reset":
                self.reset()
            case None:
                raise ValueError(
                    "Operation can't be performed before setting an operator!\n."
                )
