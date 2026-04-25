

def is_possible(n: int, s: int, upper: list[int], lower: list[int]) -> bool:
    if upper[0] == 0 or (upper[s-1]==0 and lower[s-1]==0):
        return False

    if upper[s-1] == 1:
        return True

    # przesiadka:
    for i in range(s, n):
        # 1-liner hint: sum(certain_list)>0
        if upper[i] == 1 or lower[i] == 1:
            return True

    return False

def test_all_open_direct():
    # Example 1: all stations open, direct route
    assert is_possible(5, 3, [1,1,1,1,1], [1,1,1,1,1]) == True

def test_via_end():
    # Example 2: must go to end and return on lower track
    assert is_possible(5, 4, [1,0,0,0,1], [0,1,1,1,1]) == True

def test_cannot_board_station1_closed():
    # Example 3: station 1 closed on upper track
    assert is_possible(5, 2, [0,1,1,1,1], [1,1,1,1,1]) == False

def test_destination_closed_both_tracks():
    # s open on neither track -> impossible
    assert is_possible(5, 3, [1,1,0,1,1], [1,1,0,1,1]) == False

def test_minimum_n_s_direct():
    # Smallest valid input (n=2, s=2), direct route
    assert is_possible(2, 2, [1,1], [1,1]) == True

def test_minimum_n_s_impossible():
    # n=2, s=2: upper[0]=0 -> can't board at all
    assert is_possible(2, 2, [0,1], [1,1]) == False

def test_s_equals_n_direct():
    # s == n, reachable directly on upper track
    assert is_possible(4, 4, [1,1,1,1], [1,1,1,1]) == True

def test_s_equals_n_upper_end_closed():
    # s == n but upper[n-1]=0: direct blocked, via_end also blocked (same station)
    assert is_possible(4, 4, [1,1,1,0], [1,1,1,1]) == False

def test_via_end_lower_destination_closed():
    # Can reach end on upper, but s closed on lower -> via_end fails; direct also blocked
    assert is_possible(5, 3, [1,0,0,1,1], [1,1,0,1,1]) == False

def test_direct_and_via_end_both_open():
    # Both paths available -> True
    assert is_possible(6, 4, [1,1,1,1,1,1], [1,1,1,1,1,1]) == True


def test_via_end_end_station_closed_upper():
    # switch via station 4
    assert is_possible(5, 3, [1,1,0,1,0], [1,1,1,1,1]) == True

def test_via_end_end_station_closed_lower():
    # switch via 4
    assert is_possible(5, 3, [1,0,0,1,1], [1,1,1,1,0]) == True

def test_s2_only_via_end_possible():
    # s=2, upper[1]=0 blocks direct; must go to end and come back
    assert is_possible(4, 2, [1,0,1,1], [1,1,1,1]) == True

def test_only_station1_and_s_open_on_upper():
    # All intermediate stations closed on upper — doesn't matter, train skips them
    assert is_possible(5, 4, [1,0,0,1,0], [0,0,0,1,0]) == True  # can't reach end either

def test_large_n_direct_only():
    # n=1000, s=500: only upper[0] and upper[499] open, rest closed
    upper = [0] * 1000
    upper[0] = 1
    upper[499] = 1
    lower = [0] * 1000
    assert is_possible(1000, 500, upper, lower) == True

def test_large_n_via_end_only():
    # can't board
    upper = [0] * 1000
    upper[0] = 1
    upper[498] = 1
    lower = [1] * 1000
    assert is_possible(1000, 2, upper, lower) == True