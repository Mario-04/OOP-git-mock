import numpy as np


def create_list() -> list:
    return list(range(1, 11))


def make_into_numpy_array(lst: list) -> np.ndarray:
    return np.array(lst)


if __name__ == '__main__':
    print(make_into_numpy_array(create_list()))
