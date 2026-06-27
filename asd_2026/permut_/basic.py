


import itertools

def show_them(ppl: list[list[str]]):
    for p in ppl:
        print(p)

def filter_people(ppl: list[list[str]]) -> list[list[str]]:
    res = []
    for order in ppl:
        pass



if __name__ == '__main__':
    data = [1, 2, 3]
    w = ['alice', 'bob', 'charlie', 'donald']

    perms = list(itertools.permutations(data))
    show_them(itertools.permutations(w))
