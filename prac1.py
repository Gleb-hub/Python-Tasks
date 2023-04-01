from typing import Any


def power12(x: int) -> int:
    x = x + x
    x = x + x + x
    x = x + x
    return x

def power16(x: int) -> int:
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    return x

def power15(x: int) -> int:
    y = x
    x = x + x
    x = x + x
    x = x + x
    x = x - (y - x)
    return x

def f34 (b: int, n: int, a: int) -> int: 
    x = 0
    for j in range(1, n + 1):
        y = 0
        for c in range(1, b + 1):
             y += ((34 * j + 41) ** 4 - 93 *(c + 79 + c ** 3) ** 5)
        x += y 
    
    z = 1
    for k in range(1, a + 1):
        w = 0
        for c in range(1, b + 1):
            w += (22 * (c - 8) ** 5 - k ** 4)
        z *= w

    return x - z

if __name__ == '__main__':
    print(f34(2, 2, 6))

