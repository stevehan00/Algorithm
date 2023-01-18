import math
import sys


def is_prime(n):
    if n == 1:
        return False
    num = int(math.sqrt(n))
    for k in range(2, num+1):
        if n % k == 0:
            return False
    return True


a, b = map(int, sys.stdin.readline().split())
for i in range(a, b+1):
    if is_prime(i):
        print(i)