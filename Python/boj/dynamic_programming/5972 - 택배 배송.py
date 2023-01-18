from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
inf = sys.maxsize

dp = [inf]*(n+1)

def dijkstra(start):
    dp[start] = 0
    pq = []
    heapq.heappush(pq, (0,start))

    while pq:
        w,c = heapq.heappop(pq)

        if w > dp[c]:
            continue

        for nex_w, nex_c in graph[c]:
            if nex_w+w < dp[nex_c]:
                dp[nex_c] = nex_w+w
                heapq.heappush(pq, (dp[nex_c], nex_c))

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

dijkstra(1)
print(dp[n])