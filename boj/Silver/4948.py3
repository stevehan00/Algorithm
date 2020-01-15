import math
import sys


def prime_list(n):
    sieve = [True]*n
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] is True]


while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    li = prime_list(2*n+1)
    print(len([i for i in li if i > n]))