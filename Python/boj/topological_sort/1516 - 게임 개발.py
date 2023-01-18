import sys, heapq

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
cost = [0 for _ in range(n+1)]

for i in range(1,n+1):
    lst = list(map(int, input().split()))
    cost[i] = lst[0]
    for j in range(1, len(lst)-1):
        graph[lst[j]].append(i)
    
    inDegree[i] += len(lst)-2

ans = [0 for _ in range(n+1)]
pq = []

for i in range(1,n+1):
    if inDegree[i] == 0:
        heapq.heappush(pq, (cost[i], i))
        ans[i] = cost[i]

while pq:
    cur = heapq.heappop(pq)
    for c in graph[cur[1]]:
        inDegree[c] -= 1
        
        if inDegree[c] == 0:
            nexts = cur[0]+cost[c]
            heapq.heappush(pq, (nexts, c))
            ans[c] = nexts

for c in ans[1:]:
    print(c)