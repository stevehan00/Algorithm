import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
n,m,k,x = map(int, input().split())

graph = defaultdict(list)
inf = sys.maxsize

dp = [inf for _ in range(n+1)]
heap = []

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, cur = heapq.heappop(heap)

        if dp[cur] < wei:
            continue

        for w, next_n in graph[cur]:
            next_w = wei + w

            if next_w < dp[next_n]:
                dp[next_n] = next_w
                heapq.heappush(heap, (next_w, next_n)) 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))

Dijkstra(x)

ans = []
for l in range(1, n+1):
    if dp[l] == k:
        ans.append(str(l))

if not ans:
    print(-1)
else:
    print('\n'.join(ans))