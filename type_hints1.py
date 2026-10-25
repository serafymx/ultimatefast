from collections.abc import Callable
from typing import Any

text: str = "Hello, World!"
pert: int = 5
temp: float = 36.6


def root(number: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        number (float): The number to calculate the square root of.

    Returns:
        float: The square root of the number.
    """
    return number**0.5


# we can hint a list of integers using the list[int] type hint
digits: list[int] = [1, 2, 3, 4, 5]
table: dict[str, int] = {"one": 1, "two": 2, "three": 3}
tuple_example: tuple[str, int] = ("age", 30)
tuple_example2: tuple[str, int, float] = ("height", 180, 5.9)
tuple_of_integers: tuple[int, ...] = (1, 2, 3, 4, 5)
city_names: set[str] = {"New York", "Los Angeles", "Chicago"}


dict_of_any: dict[str, Any] = {"name": "Alice", "age": 30, "is_student": True}


root_25 = root(25.0)  # This will be 5.0
root_error = root(25.0)


# first decorator function
def fence(func):
    """
    A decorator that adds a fence around the output of the decorated function.
    """
    print("Decorating function:", func.__name__)
    return func


@fence
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


print(add_numbers(5, 10))  # This will be 15


# second decorator function: to catch the output of the function and add a fence around it
# we need to define a wrapper function inside the decorator function


def fence2(func):
    def wrapper(*args, **kwargs):
        print("Decorating function:", func.__name__)
        result = func(*args, **kwargs)  # call the original function and get its result
        print("Function output:", result)
        return result

    return wrapper


@fence2
def subtract_numbers(a: int, b: int) -> int:
    """
    Subtracts the second number from the first number.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of the subtraction.
    """
    return a - b


print(subtract_numbers(10, 5))  # This will be 5


# how can we add parameter to the decorator function? we can use a closure to achieve this
def fence_with_height(height: int):
    """
    A decorator that adds a fence with the specified height around the output of the decorated function.

    Args:
        height (int): The height of the fence.

    Returns:
        callable: The decorated function with a fence.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"{'|' * height}\n{func(*args, **kwargs)}\n{'|' * height}"

        return wrapper

    # propagate the height parameter to the decorator function
    return decorator


@fence_with_height(3)
def multiply_numbers(a: int, b: int) -> int:
    """
    Multiplies two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b


print(multiply_numbers(5, 10))  # This will be 50 with a fence of height 3


# hintin that the argument is a function is done using
# the Callable type hint from the typing module


def process_function(func: Callable[[int, int], int]) -> int:
    return func(5, 10)
