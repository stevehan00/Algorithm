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

N,E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

a,b = map(int, sys.stdin.readline().split())

lst = [1, a, b, N, a]
ans1 = 0
ans2 = 0
flag1 = True
flag2 = True

for i in range(len(lst)-2):
    dp = [inf]*(N+1)
    heap = []

    Dijkstra(lst[i])

    if dp[lst[i+1]] != inf:
        ans1 += dp[lst[i+1]]
    else:
        flag1 = False

    if dp[lst[i+2]] != inf:
        ans2 += dp[lst[i+2]]
    else:
        flag2 = False

if not flag1:
    ans1 = inf

if not flag2:
    ans2 = inf

if flag1 or flag2:
    print(min(ans1, ans2))
else:
    print(-1)