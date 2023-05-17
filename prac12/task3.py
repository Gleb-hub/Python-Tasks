import math
import deal
from raises import raises

distance_function = deal.chain(
    deal.pre(lambda x, y: None not in [x, y]),
    deal.pre(lambda x, y: [] not in [x, y]),
    deal.pre(lambda x, y: isinstance(x, list | tuple) and isinstance(y, list | tuple)),
    deal.pre(lambda x, y: len(x) == len(y)),
    deal.pre(lambda x, y: all([isinstance(i, int | float) and isinstance(j, int | float) for i, j in zip(x, y)])),
    deal.has(),
    deal.post(lambda res: isinstance(res, int | float)),
    deal.post(lambda res: res >= 0)
)


@distance_function
def euclidean_distance(x, y):
    """

    >>> euclidean_distance([0, 0], [3, 4])
    5.0
    """
    return math.sqrt(sum((x_i - y_i) ** 2 for x_i, y_i in zip(x, y)))


@distance_function
def manhattan_distance(x, y):
    """

    >>> manhattan_distance([0, 0], [3, 4])
    7
    """
    return sum(abs(i - j) for i, j in zip(x, y))
