import sys

n,m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

inf = sys.maxsize
bf = [inf]*(n+1)

bf[1] = 0

minus = False

for i in range(n):
    for j in range(m):
        u = graph[j][0]
        v = graph[j][1]
        w = graph[j][2]

        if bf[u] != inf and bf[v] > bf[u] + w:
            bf[v] = bf[u] + w
            if i == n-1:
                minus = True

if minus:
    print(-1)
else:
    for i in range(2,n+1):
        if bf[i] == inf:
            print(-1)
        else:
            print(bf[i])