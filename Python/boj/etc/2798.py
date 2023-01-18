from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

result = set(combinations(lst, 3))
dis = m


for i in result:
    temp = sum(i)
    if temp > m:
        continue
    if (m-temp) < dis:
        dis = m-temp
        t = temp

print(t)