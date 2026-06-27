


class Plane:
    def __init__(self, initial_occupation: set[int]):
        self.seats = set()
        self.seats.update(initial_occupation)

    def is_contiguous(self) -> bool:
        pass

    def add(self, seat: int):
        pass

    def remove(self, seat: int):
        pass

import pytest


@pytest.fixture
def empty_plane():
    return Plane(set())


@pytest.fixture
def contiguous_plane():
    return Plane({1, 2, 3, 4})


@pytest.fixture
def non_contiguous_plane():
    return Plane({1, 3, 5})



class TestIsContiguous:
    def test_empty_is_contiguous(self, empty_plane):
        assert empty_plane.is_contiguous() is True

    def test_single_seat_is_contiguous(self):
        assert Plane({5}).is_contiguous() is True

    def test_contiguous(self, contiguous_plane):
        assert contiguous_plane.is_contiguous() is True

    def test_non_contiguous(self, non_contiguous_plane):
        assert non_contiguous_plane.is_contiguous() is False


class TestAdd:
    def test_add_new_seat(self, empty_plane):
        empty_plane.add(1)
        assert 1 in empty_plane.seats

    def test_add_duplicate(self, contiguous_plane):
        contiguous_plane.add(1)
        assert contiguous_plane.seats == {1, 2, 3, 4}

    def test_add_makes_contiguous(self, non_contiguous_plane):
        non_contiguous_plane.add(2)
        non_contiguous_plane.add(4)
        assert non_contiguous_plane.is_contiguous() is True


class TestRemove:

    def test_remove_breaks_contiguity(self, contiguous_plane):
        contiguous_plane.remove(2)
        assert contiguous_plane.is_contiguous() is False

    def test_remove_nonexistent(self, empty_plane):
        with pytest.raises(KeyError):
            empty_plane.remove(99)