from collections import defaultdict
import heapq, sys

def prim(start):
    mst = []
    visit[start] = True

    sums = 0
    cnt = 1

    for a in adj[start]:
        heapq.heappush(mst, a)
    while mst:
        c,v = heapq.heappop(mst)
        if not visit[v]:
            visit[v] = True
            sums += c
            cnt += 1
            for a in adj[v]:
                heapq.heappush(mst, a)

        if cnt == n:
            return sums

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    u,v,c = map(int, sys.stdin.readline().split())
    adj[u].append([c,v])
    adj[v].append([c,u])

d = prim(1)

print(d)