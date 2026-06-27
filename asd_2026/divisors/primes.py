


def primes(MX):
    sieve = [True] * (MX + 1)
    sieve[:2] = [False, False]
    for i in range(2, int(MX**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return [i for i, p in enumerate(sieve) if p]

def test_one():
    x = len(primes(10**8))
    print(x)

if __name__ == '__main__':
    print(primes(100))
