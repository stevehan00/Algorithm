from collections import defaultdict
import sys, heapq

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, cur = heapq.heappop(heap)

        if dp[cur] < wei:
            continue

        for w, next_n in graph[cur]:
            next_w = w + wei

            if next_w < dp[next_n]:
                dp[next_n] = next_w
                heapq.heappush(heap, (next_w, next_n))

inf = sys.maxsize
n, m, x = map(int , sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

dp = [inf]*(n+1)
heap = []

Dijkstra(x)

ans_l = dp.copy()
ans_l[0]=-1

for c in range(1, n+1):

    if ans_l[c] != inf:
        dp = [inf]*(n+1)
        heap = []
        Dijkstra(c)
        if dp[x] != inf:
            ans_l[c] += dp[x]
        else:
            ans_l[c] = -1
    else:
        ans_l[c] = -1

print(max(ans_l))