"""Measure the execution time of a function."""

import time


def running_2000(function, *args, **kwargs):
    """Execute a function and return its elapsed time in seconds."""
    start_time = time.perf_counter()
    function(*args, **kwargs)
    return time.perf_counter() - start_time


if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000("Hi {name}".format, name="Bug"))
