# src/main.py
import argparse

from sample_package.sample_module import factorial

from main_package.helpers import greet


def main():
    parser = argparse.ArgumentParser(
        description="A simple argparse example with local and external dependencies"
    )
    parser.add_argument(
        "--name", type=str, required=True, help="Name of the person to greet"
    )
    parser.add_argument(
        "--factorial", type=int, help="Calculate factorial of this number"
    )
    args = parser.parse_args()

    greeting_message = greet(args.name)
    print(greeting_message)

    print(factorial(1))


if __name__ == "__main__":
    main()
