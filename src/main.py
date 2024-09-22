# src/main.py
import argparse

from helpers import greet


def main():
    parser = argparse.ArgumentParser(
        description="A simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependencyA simple argparse example with local dependency"
    )
    parser.add_argument(
        "--name", type=str, required=True, help="Name of the person to greet"
    )

    args = parser.parse_args()

    greeting_message = greet(args.name)
    print(greeting_message)


if __name__ == "__main__":
    main()
