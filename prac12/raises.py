import math
from contextlib import contextmanager


@contextmanager
def raises(e):
    try:
        yield
    except e:
        pass


if __name__ == '__main__':
    with raises(ZeroDivisionError):
        1 / 0
    with raises(ValueError):
        math.sqrt(-1)
