#!/usr/bin/env python3

from calculator.calculator import Calculator


def main():
    calculator = Calculator()

    while True:
        expression = input("Enter your expression: ").strip()
        if expression in ("exit", "quit"):
            break

        try:
            print(calculator.calculate(expression))
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
