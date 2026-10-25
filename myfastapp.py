from collections.abc import Callable
from typing import Any

routes: dict[str, Callable[[Any], Any]] = {}


def route(path: str):
    def register_route(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        routes[path] = func
        return func

    return register_route


@route("/hello")
def hello(hello_name: str) -> str:
    return f"Hello, {hello_name}!"


request: str = ""

while request != "exit":
    request = input("Enter a route (or 'exit' to quit): ")
    if request in routes:
        name = input("Enter your name: ")
        response = routes[request](name)
        print(response)
    elif request != "exit":
        print("Route not found.")
