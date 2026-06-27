


# def solve(a: int, b:int) -> tuple[int, int]:
#     # https://codeforces.com/problemset/problem/2137/C
#     # return - greatest a+b, divisor k used to get it
#     # przejść pętlą po wszystkich `k`, sprawdzić czy są dzielnikami b, sprawdzić sumę, i jak jest lepsza i parzysta, to
#     # zapamiętać
#
#     w = [((a* k + b//k), k) for k in range(1, b+1) if b % k == 0 and (a*k + b/k) % 2 == 0]
#     return (0,0) if not w else max(w)


def solve(a: int, b:int) -> tuple[int, int]:
    best = (0,0)
    for k in range(1, b+1):
        if b % k != 0: continue
        ss = a * k + b // k
        if ss % 2 != 0: continue
        best = max(best, (ss,k))
    return best






if __name__ == '__main__':
    for a in range(1, 20):
        for b in range(1, 20):

            ss = solve(a, b)
            candidates = [b, b//2]
            if ss[0]>0:
                # if ss[1] not in candidates:
                print(f'{a=:3}, {b=:3}, {ss=}')
