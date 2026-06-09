"""main.py — demonstrate the basic_math C++ extension built with pybind11."""

from basic_math import add

if __name__ == "__main__":
    a, b = 3, 4
    result = add(a, b)
    print(f"add({a}, {b}) = {result}")

    # Show that the docstring travelled from C++ to Python
    print("\nDocstring from C++:")
    print(add.__doc__)