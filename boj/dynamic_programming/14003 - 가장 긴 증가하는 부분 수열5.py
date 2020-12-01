from bisect import bisect_left
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dp = [lst[0]]
p = [0 for _ in range(n)]
p[0] = 0

for i in range(1, n):
    if dp[-1] < lst[i]:
        p[i] = len(dp)
        dp.append(lst[i])
    else:
        idx = bisect_left(dp, lst[i])
        p[i] = idx
        dp[idx] = lst[i]

ll = []

cnt = len(dp)-1
for i in range(n-1, -1, -1):
    if p[i] == cnt:
        cnt -= 1
        ll.append(lst[i])

print(len(dp))
print(*ll[::-1])