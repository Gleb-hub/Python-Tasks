import numpy as np
import matplotlib.pyplot as plt


def noise(x: float, y: float) -> float:
    return (5.0 * np.sin(1.1 * (x + y))) * 123.123123123123 % 1


def draw():  
    x = list(range(0, 1000))
    y = list(range(0, 1000))
    
    res: list[float] = []

    for x_coord, y_coord in zip(x, y):
        res.append(noise(x_coord, y_coord))

    plt.figure(figsize=(18, 6))
    plt.plot(res)
    plt.show()

if __name__ == "__main__":
    draw()



