from collections import defaultdict
import sys, heapq

t = int(sys.stdin.readline())
inf = sys.maxsize

for _ in range(t):
    n,d,c = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)

    for _ in range(d):
        a,b,s = map(int, sys.stdin.readline().split())
        graph[b].append((s,a))
    
    p = []
    dp = [inf]*(n+1)
    dp[c] = 0
    heapq.heappush(p, (0, c))

    while p:
        cur_w,cur_n = heapq.heappop(p)

        if dp[cur_n] < cur_w:
            continue

        for nw, nn in graph[cur_n]:
            nexts = cur_w + nw
            if dp[nn] > nexts:
                dp[nn] = nexts
                heapq.heappush(p, (nexts, nn))
    
    cnt = 0
    maxs = 0

    for c in dp:
        if c != inf:
            cnt += 1
            maxs = max(maxs, c)
    
    print(cnt,maxs)