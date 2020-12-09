import sys,heapq

inf = sys.maxsize

def dijkstra(start):
    dp = [inf for _ in range(n)]
    dp[start] = 0
    pq = []

    heapq.heappush(pq, (0, start))

    while pq:
        w, cur = heapq.heappop(pq)

        if dp[cur] < w:
            continue

        for n_w, n_n in graph[cur]:
            wei = w + n_w
            
            if dp[n_n] > wei and check[cur][n_n] == 0:
                dp[n_n] = wei
                heapq.heappush(pq, (wei, n_n))
    return dp

while True:
    n,m = map(int, sys.stdin.readline().split())
    if n == m == 0:
        break
    s,d = map(int, sys.stdin.readline().split())

    graph = [set() for _ in range(n)]
    graph_r = [set() for _ in range(n)]

    for _ in range(m):
        u,v,p = map(int, sys.stdin.readline().split())
        graph[u].add((p,v))
        graph_r[v].add((p,u))

    check = [[0]*n for _ in range(n)]
    dp = dijkstra(s)

    q = []
    q.append(d)
    while q:
        cur = q.pop()
        for c in graph_r[cur]:
            if dp[cur] == dp[c[1]] + c[0]:
                check[c[1]][cur] = 1
                q.append(c[1])

    dp = dijkstra(s)

    if dp[d] == inf:
        print(-1)
    else:
        print(dp[d])