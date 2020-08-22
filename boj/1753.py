from collections import defaultdict
import heapq
import sys

inf = sys.maxsize

V, E = map(int ,sys.stdin.readline().split())
k = int(sys.stdin.readline())

dp = [inf]*(V+1)
heap = []
graph = defaultdict(list)

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


for _ in range(E):
    u, v, w = map(int ,sys.stdin.readline().split())
    graph[u].append((w, v))

Dijkstra(k)

for i in range(1, V+1):
    print("INF" if dp[i] == inf else dp[i])