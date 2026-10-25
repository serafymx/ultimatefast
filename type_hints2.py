def fence():
    """
    A simple function that returns a string representing a fence.
    """
    return "||"


def fencer(func):
    """
    A decorator that adds a fence around the output of the decorated function.

    """

    def wrapper(*args, **kwargs):
        return f"{fence()}\n{func(*args, **kwargs)}\n{fence()}"

    return wrapper


def fence_with_height(height: int) -> str:
    """
    Returns a string representing a fence with the specified height.
    """
    return "||\n" * height


def fence_with_height_decorator(height: int):
    """
    A decorator that adds a fence with the specified height around the output of the decorated function.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"{fence_with_height(height)}{func(*args, **kwargs)}\n{fence_with_height(height)}"

        return wrapper

    return decorator


@fence_with_height_decorator(3)
def add_numbers(a: int, b: int) -> int:
    """The sum of the two numbers."""
    return a + b


if __name__ == "__main__":
    print(add_numbers(5, 10))
