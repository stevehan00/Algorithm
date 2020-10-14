import sys, heapq
from collections import defaultdict


def Dstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, cur = heapq.heappop(heap)

        if dp[cur] < w:
            continue

        for weight, next_n in graph[cur]:
            next_w = w + weight

            if next_w < dp[next_n]:
                dp[next_n] = next_w
                heapq.heappush(heap, (next_w, next_n))

for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(m):        
        a,b,w = map(int, sys.stdin.readline().split())
        graph[a].append((w,b))
        graph[b].append((w,a))

    k = int(sys.stdin.readline())
    ipt = set(map(int, sys.stdin.readline().split()))

    inf = sys.maxsize

    result = [0]*n

    for c in ipt:
        dp = [inf]*(n+1)
        heap = []

        Dstra(c)
        
        for l in range(1,n+1):
            result[l-1] += dp[l]
    print(result.index(min(result))+1)
