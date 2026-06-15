

def is_bracket_correct(bra: str, mask: int) -> bool:
    sum_ = 0
    for pos, ch in enumerate(bra):
        # if mask here is 0 --> continue
        if sum_ < 0: return False
        if ch == '(':
            sum_ += 1
        else:
            sum_ -= 1
    return sum_ == 0



def minimal_deletion(bra: str) -> int:
    # how many brackets to remove to get a correct bracket

    # 1) zmodyfikować is bracket correct tak by akceptował maskę
    #    - powinien ignorować pozycje na których maska = 0
    #
    # 2) loop over all masks not longer than `bra`;
    # check if they lead to correct bracket
    # note them if the number of `0`s in mask is lower then previous
    return 0



def test_bra_1():
    assert is_bracket_correct('()') == True
    assert is_bracket_correct('()()()')
    assert is_bracket_correct('(()())')

    assert is_bracket_correct(')') == False
    assert is_bracket_correct(')(') == False

def test_bra_2():
    assert is_bracket_correct('((())') == False


if __name__ == '__main__':
    pass