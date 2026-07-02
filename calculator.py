#!/usr/bin/env python3

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo by zero")
    return x % y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if not isinstance(x, int) or x != int(x):
        raise ValueError("Factorial is only defined for integers")
    return math.factorial(int(x))

def main():
    print("Advanced Calculator")
    print("-" * 40)
    print("Binary Operations: +, -, *, /, **, %")
    print("  Examples: 10 + 5, 2 ** 3, 10 % 3")
    print("Unary Operations: sqrt, factorial")
    print("  Examples: sqrt 16, factorial 5")
    print("Type 'quit' to exit")
    print("-" * 40)

    while True:
        try:
            user_input = input("\nEnter calculation: ").strip()

            if user_input.lower() == 'quit':
                print("Thank you for using the calculator!")
                break

            parts = user_input.split()

            if not parts:
                print("Invalid input. Please enter a calculation.")
                continue

            # Handle unary operations (sqrt, factorial)
            if parts[0].lower() in ['sqrt', 'factorial']:
                if len(parts) != 2:
                    print("Invalid format. Use: operation number")
                    continue

                operation = parts[0].lower()
                try:
                    num = int(parts[1])
                except ValueError:
                    print("Invalid number entered.")
                    continue

                if operation == 'sqrt':
                    result = square_root(num)
                    print(f"Result: sqrt({num}) = {result}")
                elif operation == 'factorial':
                    result = factorial(num)
                    print(f"Result: factorial({int(num)}) = {result}")

            # Handle binary operations
            elif len(parts) == 3:
                num1_str, operator, num2_str = parts

                try:
                    num1 = float(num1_str)
                    num2 = float(num2_str)
                except ValueError:
                    print("Invalid numbers entered.")
                    continue

                if operator == '+':
                    result = add(num1, num2)
                elif operator == '-':
                    result = subtract(num1, num2)
                elif operator == '*':
                    result = multiply(num1, num2)
                elif operator == '/':
                    result = divide(num1, num2)
                elif operator == '**':
                    result = power(num1, num2)
                elif operator == '%':
                    result = modulo(num1, num2)
                else:
                    print("Invalid operator. Use +, -, *, /, **, or %")
                    continue

                print(f"Result: {num1} {operator} {num2} = {result}")

            else:
                print("Invalid format. Use: number operator number")
                print("Or: operation number (for sqrt, factorial)")
                continue

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
