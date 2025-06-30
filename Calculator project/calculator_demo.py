from calculator import Calculator

def main():
    """
    Demo code for the calculator.
    """

    calculator = Calculator()
    while True:
        print(f"{calculator}\n")
        if gather_input(calculator):
            print("Session is over.")
            break


def gather_input(calculator):
    """
    Gets user input, performs chosen operation, and shows errors if any.

    Returns:
        bool: True if user wants to finish, False if not.
    """
    i = (
        input(
            "What's your operation?\n"
            "Choose from: '+', '-', '*', '/', 'root' or 'reset'. Input 'finish' to end.\n"
        )
        .strip()
        .lower()
    )
    if i == "finish":
        print("Calculation is finished.")
        return True
    if i == "root":
        try:
            n = int(input("Enter the degree of the root:").strip())
        except ValueError:
            print("The degree must be an integer.")
            return False
        try:
            calculator.check_operator("root")
            calculator.perform_operation(n)
        except (ValueError, ZeroDivisionError) as text:
            print(text)
            return False

    elif i == "reset":
        try:
            calculator.check_operator("reset")
            calculator.perform_operation()
        except ValueError as text:
            print(text)
            return False
    else:
        try:
            x = float(input("Provide number:\n").strip())
        except ValueError:
            print("Invalid input. Provide a number!\n")
            return False
        try:
            calculator.check_operator(i)
            calculator.perform_operation(x)
        except (ValueError, ZeroDivisionError) as text:
            print(text)
            return False


if __name__ == "__main__":
    main()
