def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def percentage(x, y):
    return (x / y) * 100

def calculator():
    """
    A simple calculator function that allows the user to perform basic arithmetic operations.

    The user can select from the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage

    The function prompts the user to enter their choice of operation and two numeric values.
    It then performs the selected operation and prints the result.

    Exceptions:
    - If the user inputs a non-numeric value for the numbers, an error message is displayed.
    - If any other error occurs during execution, an error message is displayed.

    Returns:
    None
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    try:
        choice = input("Enter choice(1/2/3/4/5): ")

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
    except Exception as e:
        print(f"An error occurred: {e}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} is {percentage(num1, num2)}% of {num2}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()