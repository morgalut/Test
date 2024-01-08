# test_script.py
import argparse
from TOOLS import col
from TOOLS.numbers import simp, comp

def main():
    parser = argparse.ArgumentParser(description='Test script with command-line arguments.')
    parser.add_argument('command', choices=['col', 'simp', 'comp'], help='Specify the command to execute.')

    args = parser.parse_args()

    try:
        if args.command == 'col':
            # Example usage of col.py
            col_result = col.myzip([1, 2, 3], ['a', 'b', 'c'], 'output')
            print("Result of col.myzip:", col_result)
        elif args.command == 'simp':
            # Example usage of simp.py
            simp_instance = simp.SomeClass()
            simp_instance.some_method()
        elif args.command == 'comp':
            # Example usage of comp.py
            comp.another_function()
        else:
            raise ValueError("Invalid command. Please specify 'col', 'simp', or 'comp'.")
    except Exception as e:
        print(f"Error executing command '{args.command}': {e}")

if __name__ == "__main__":
    main()
