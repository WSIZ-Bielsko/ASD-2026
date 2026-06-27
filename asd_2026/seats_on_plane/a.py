def is_contiguous(a: set[int]) -> bool:
    if len(a) == 0:
        return True
    mi_ = min(a)
    mx_ = max(a)
    return len(a) == mx_ - mi_ + 1

def test_contiguous():
    assert is_contiguous({1, 2, 3}) is True
    assert is_contiguous({1, 3, 2}) is True
    assert is_contiguous({1, 3, 5}) is False


def test_some_more():
    assert is_contiguous({1, 2, 3}) is True
    assert is_contiguous({3, 2, 1}) is True
    assert is_contiguous({1, 3, 2}) is True
    assert is_contiguous({10, 11, 12, 13}) is True
    assert is_contiguous({1, 3}) is False
    assert is_contiguous({1, 2, 4}) is False
    assert is_contiguous({5}) is True
    assert is_contiguous(set()) is True
    assert is_contiguous({-1, 0, 1}) is True


if __name__ == '__main__':
    pass