#!/usr/bin/env python3

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

def main():
    print("Simple Calculator")
    print("-" * 30)
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    print("-" * 30)

    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 10 + 5): ").strip()

            if user_input.lower() == 'quit':
                print("Thank you for using the calculator!")
                break

            parts = user_input.split()

            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue

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
            else:
                print("Invalid operator. Use +, -, *, or /")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
