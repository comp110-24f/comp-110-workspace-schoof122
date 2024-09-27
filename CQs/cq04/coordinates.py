"""Contains a function to get coordinates"""

__author__ = "730674279"


def get_coords(xs: str, ys: str) -> None:
    """Provides coordinates to a user"""
    idx_x: int = 0
    idx_y: int = 0
    while idx_x < len(xs):
        idx_y = 0
        while idx_y < len(ys):
            print(f"({xs[idx_x]},{ys[idx_y]})")
            idx_y += 1
        idx_x += 1
