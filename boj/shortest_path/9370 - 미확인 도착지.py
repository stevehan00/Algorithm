from collections import defaultdict
import sys, heapq

def Dijkstra(start):
    pq = []
    dp = [INF]*(n+1)
    dp[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cur_w, cur_n = heapq.heappop(pq)

        if dp[cur_n] < cur_w:
            continue

        for ww,nn in graph[cur_n]:
            nexts = ww +cur_w

            if nexts < dp[nn]:
                dp[nn] = nexts
                heapq.heappush(pq, (nexts,nn))

    return dp

T = int(sys.stdin.readline())
INF = sys.maxsize

for _ in range(T):
    n,m,t = map(int, sys.stdin.readline().split())
    s,g,h = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    target = []

    imp_path = 0

    for _ in range(m):
        a,b,d = map(int, sys.stdin.readline().split())
        graph[a].append((d,b))
        graph[b].append((d,a))

        if (a == g and b == h) or (a == h and b == g):
            imp_path = d
    
    for _ in range(t):
        target.append((int(input())))
    
    dp = Dijkstra(s)

    dp1 = Dijkstra(h) # h-> target
    dp2 = Dijkstra(g) # g -> target
    

    ans = []

    for c in target:
        if (dp[g] + dp2[h] + dp1[c] == dp[c]) or (dp[h] + dp1[g] + dp2[c] == dp[c]):
            ans.append(c)

    for c in sorted(ans):
        print(c, end=' ')
    print()