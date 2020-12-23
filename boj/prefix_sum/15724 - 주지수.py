import sys

n,m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

pref = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        pref[i+1][j+1] = pref[i][j+1] + pref[i+1][j] - pref[i][j] + lst[i][j]

k = int(sys.stdin.readline())
for _ in range(k):
    lr, lc, rr, rc = map(int, sys.stdin.readline().split())
    print(pref[rr][rc] - pref[rr][lc-1] - pref[lr-1][rc] + pref[lr-1][lc-1])