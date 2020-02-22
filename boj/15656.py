from itertools import product
import sys

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))

for i in list(product(lst, repeat = m)):
    for j in i:
        print(j, end=' ')
    print()