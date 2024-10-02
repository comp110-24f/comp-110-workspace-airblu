"""print formatted pairs"""

__author__ = "730643371"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        while idx2 < len(ys):
            print(xs[idx1] + "," + ys[idx2])
            idx2 += 1
        idx2 = 0
        idx1 += 1
