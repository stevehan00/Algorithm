import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = sys.maxsize

weight = [[inf for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    weight[s][e] = min(weight[s][e], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                weight[i][j] = 0
            else:
                weight[i][j] = min(weight[i][j], weight[i][k]+weight[k][j])


for r in weight[1:]:
    for c in r[1:]:
        if c == inf:
            print(0, end=' ')
        else:
            print(c, end=' ')
    print()