from copy import copy, deepcopy
type Graph = dict[int, list[int]]


if __name__ == '__main__':
    a = {1,2,3}
    b = {2,1,3}
    assert a == b


    d = {}
    d[11] = [1,2,3]

    gg = deepcopy(d)
    # gg = copy(d)
    print(gg)
    d[11].append(4)
    print(gg)


