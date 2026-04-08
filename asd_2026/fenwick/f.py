import sys
from abc import ABC, abstractmethod

from asd_2026.common.utils import ts


class RangeSumQuery(ABC):
    @abstractmethod
    def add(self, i: int, delta: int) -> None:
        """Add delta to the element at index i (1-based)."""

    @abstractmethod
    def query(self, i: int) -> int:
        """Get the prefix sum from index 1 to i (1-based)."""

    @abstractmethod
    def query_range(self, left: int, right: int) -> int:
        """Get the sum in the inclusive range [left, right] (1-based)."""


class MyRangeSumQuery(RangeSumQuery):
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, i: int, delta: int) -> None:
        self.tree[i] += delta

    def query(self, i: int) -> int:
        return sum(self.tree[:i + 1])

    def query_range(self, left: int, right: int) -> int:
        return sum(self.tree[left: right + 1])


class FenwickTree(RangeSumQuery):
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, i: int, delta: int) -> None:
        """Add delta to the element at index i (1-based)."""
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        """Get the prefix sum from index 1 to i (1-based)."""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

    def query_range(self, left: int, right: int) -> int:
        """Get the sum in the inclusive range [left, right] (1-based)."""
        return self.query(right) - self.query(left - 1)


def test1():
    # ft = FenwickTree(99999)  # Initialize for an array of size 10
    ft = MyRangeSumQuery(99999)  # Initialize for an array of size 10
    ft.add(3, 5)  # Add 5 at index 3
    ft.add(5, 2)  # Add 2 at index 5

    print(ft.query(4))  # Output: 5 (sum from index 1 to 4)
    print(ft.query(6))  # Output: 7 (sum from index 1 to 6)

    ft.add(4, -2)
    print(ft.query(4))  # Output: 3 (sum from index 1 to 4)
    print(ft.query(6))  # Output: 5 (sum from index 1 to 6)


if __name__ == '__main__':
    SIZE = 2 * 10 ** 6
    # tt = MyRangeSumQuery(SIZE)
    tt = FenwickTree(SIZE)

    print(f'size : {sys.getsizeof(tt.tree):,}')

    N = 100
    st = ts()
    x = 0
    for _ in range(N):
        x += tt.query(SIZE-1)
    elapsed = ts() - st
    print(f'elapsed: {elapsed:.3f}s')