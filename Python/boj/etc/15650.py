from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]

for i in combinations(nums, m):
    for j in i:
        print(j, end=' ')
    print()