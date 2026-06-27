from random import randint, seed

if __name__ == '__main__':
    seed(111)
    w = [randint(1,101) for _ in range(15)]
    print(w)