import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result

    return wrapper


@timer
def make_list(n):
    return list(range(1, n + 1))


if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = make_list(n)
    print(f"Output: {result}")
