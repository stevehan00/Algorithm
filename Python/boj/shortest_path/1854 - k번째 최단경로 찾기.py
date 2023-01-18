from collections import defaultdict
import sys,heapq

n,m,k = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
inf = sys.maxsize

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))

nodehpq = [[] for _ in range(n+1)]

pq = []
heapq.heappush(pq, (0, 1))
heapq.heappush(nodehpq[1], 0)

while pq:
    cur_w, cur_n = heapq.heappop(pq)

    for nw, nn in graph[cur_n]:
        nexts = cur_w + nw

        if len(nodehpq[nn]) < k:
            heapq.heappush(nodehpq[nn], -nexts)
            heapq.heappush(pq, (nexts, nn))
        else:
            temp = -heapq.heappop(nodehpq[nn])
            if temp > nexts:
                heapq.heappush(nodehpq[nn], -nexts)
                heapq.heappush(pq, (nexts, nn))
            else:
                heapq.heappush(nodehpq[nn], -temp)


for i in range(1,n+1):
    if len(nodehpq[i]) < k:
        print(-1)
    else:
        print(-heapq.heappop(nodehpq[i]))