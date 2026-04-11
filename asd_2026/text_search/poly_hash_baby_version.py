

def sum_hash(source, start, end) -> int:
    return sum([ord(c) for c in source[start:end]])

def find_candidates(source, target) -> list[int]:
    xsum = sum_hash(target, 0, len(target))
    beg = 0
    end = len(target)
    csum = sum_hash(source, 0, len(target))
    positions = []
    if csum == xsum:
        positions.append(0)

    while end < len(source)-1:
        csum = csum - ord(source[beg]) + ord(source[end+1])
        beg += 1
        end += 1
        if csum == xsum:
            positions.append(beg)

    return positions

if __name__ == '__main__':
    # d = 'zz'
    # print(ord(d[0]))
    # print(sum_hash(d, 0, 2))

    s = 'lorem ipsum dolor sit amet dolor Greenland'
    sss = 'dolor'
    # pos = s.find(sss)
    # print(sum_hash(sss, 0, 10**9)) # 544

    cnd = find_candidates(s, sss)
    # true positions = 12, 27
    print(cnd)
    for c in cnd:
        if s[c:c+len(sss)] == sss:
            print(c)
