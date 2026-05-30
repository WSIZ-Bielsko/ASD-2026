from collections import deque

if __name__ == '__main__':
    r = 2+16
    print(bin(r))
    zz = r & (-r)
    print(bin(zz))

    print('---')
    z = 0 & (-0)
    print('z=', bin(z))

    d = deque()

    s = {1: 1, 2: 20}


    for k in s:
        print(k)