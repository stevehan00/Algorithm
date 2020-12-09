from collections import defaultdict
import sys, heapq

inf = sys.maxsize

def dijkstra():
    dp[1][0] = 0
    pq = []

    heapq.heappush(pq, (0, 0, 1))

    while pq:
        cost, time, loc = heapq.heappop(pq)

        if dp[loc][cost] < time:
            continue

        for c in graph[loc]:
            n_cost = cost + c[1]
            n_time = time + c[2]

            if n_cost > m:
                continue

            if dp[c[0]][n_cost] > n_time:
                for i in range(n_cost, m+1):
                    if dp[c[0]][i] > n_time:
                        dp[c[0]][i] = n_time
                heapq.heappush(pq, (n_cost, n_time, c[0]))



t = int(sys.stdin.readline())

for _ in range(t):
    n,m,k = map(int, sys.stdin.readline().split())
    graph = defaultdict(set)
    dp = [[inf]*(m+1) for _ in range(n+1)]

    for _ in range(k):
         u,v,c,d = map(int, sys.stdin.readline().split())
         graph[u].add((v,c,d))

    dijkstra()

    ans = min(dp[-1])

    if ans == inf:
        print('Poor KCM')
    else:
        print(ans)