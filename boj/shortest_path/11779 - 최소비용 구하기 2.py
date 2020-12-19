from collections import defaultdict
import sys,heapq

def stra(start):
    p = []
    heapq.heappush(p, (0,start))
    dp[start] = 0

    while p:
        cur_w, cur_n = heapq.heappop(p)

        if cur_w > dp[cur_n]:
            continue

        for w, nn in graph[cur_n]:
            nw = w + cur_w

            if dp[nn] > nw:
                parent[nn] = cur_n
                dp[nn] = nw
                heapq.heappush(p, (nw, nn))



n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = defaultdict(list)
parent = [0]*(n+1)

for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

s,e = map(int, input().split())

inf = sys.maxsize
dp = [inf]*(n+1)

stra(s)

path = []
temp = e
while temp != s:
    path.append(temp)
    temp = parent[temp]

path.append(s)

print(dp[e])
print(len(path))
print(*path[::-1])