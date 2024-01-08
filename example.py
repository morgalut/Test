# example.py
from TOOLS import col
from TOOLS.numbers import simp, comp

if __name__ == "__main__":
    print("Executing example.py")

    # Example usage of col.py
    col_result = col.myzip([1, 2, 3], ['a', 'b', 'c'], 'output')
    print("Result of col.myzip:", col_result)

    # Example usage of simp.py
    simp_instance = simp.SomeClass()
    simp_instance.some_method()

    # Example usage of comp.py
    comp.another_function()
