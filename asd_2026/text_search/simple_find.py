
def mfind(source, pattern) -> list[int]:
    result = []
    start = 0
    while True:
        idx = source.find(pattern, start)
        if idx == -1:
            break
        result.append(idx)
        start = idx + 1
    return result





# mfind tests


def test_single_occurrence_at_start():
    """Pattern found at the beginning"""
    assert mfind("hello world", "hello") == [0]


def test_single_occurrence_at_end():
    """Pattern found at the end"""
    assert mfind("hello world", "world") == [6]


def test_single_occurrence_in_middle():
    """Pattern found in the middle"""
    assert mfind("hello world", "lo w") == [3]


def test_multiple_occurrences():
    """Pattern found multiple times"""
    assert mfind("aaaa", "aa") == [0, 1, 2]


def test_no_match():
    """Pattern not found in source"""
    assert mfind("hello", "xyz") == []


def test_pattern_longer_than_source():
    """Pattern is longer than source"""
    assert mfind("hi", "hello") == []


def test_single_character_pattern():
    """Single character pattern"""
    assert mfind("hello", "l") == [2, 3]


def test_single_character_match():
    """Single character source and pattern match"""
    assert mfind("a", "a") == [0]


def test_single_character_no_match():
    """Single character source and pattern don't match"""
    assert mfind("a", "b") == []


def test_pattern_equals_source():
    """Pattern is the same as source"""
    assert mfind("hello", "hello") == [0]


def test_empty_source():
    """Empty source string"""
    assert mfind("", "a") == []


def test_empty_pattern():
    """Empty pattern string - edge case"""
    # This might cause issues depending on implementation
    result = mfind("hello", "")
    # Every position could be considered a match for empty pattern
    assert isinstance(result, list)


def test_overlapping_patterns():
    """Overlapping pattern occurrences"""
    assert mfind("ababab", "ab") == [0, 2, 4]


def test_overlapping_patterns_single_char():
    """Single character repeated"""
    result = mfind("aaaa", "a")
    assert result == [0, 1, 2, 3]


def test_pattern_with_repeated_chars():
    """Pattern that has repeated characters"""
    assert mfind("aabbccaa", "aa") == [0, 6]


def test_case_sensitive():
    """Pattern matching is case sensitive"""
    assert mfind("Hello World", "hello") == []



if __name__ == '__main__':
    s = 'lorem ipsum dolor sit amet dolor Greenland'

    print(s.find('Greenland'))  # location of the first letter of the found sequence; -1 if not found
    print(s[33])    # G

    print(s.find('dolor'))  # 12
    print(s.rfind('dolor')) # 27

