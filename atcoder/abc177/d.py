import sys
from collections import defaultdict
 
graph = defaultdict(set)
 
n, m = map(int, sys.stdin.readline().split())
 
if m == 0:
    print(1)
    exit()
 
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
 
    if not b in graph[a]:
        graph[a].add(b)
    if not a in graph[b]:
        graph[b].add(a)
 
visited = set()
maxi = 0
 
def dfs(start):
    stk = [start]
    visited.add(start)
    temp = 1
 
    while stk:
        cur = stk.pop()
 
        for c in graph[cur]:
            if not c in visited:
                visited.add(c)
                stk.append(c)
                temp += 1
 
    return temp
 
for j in graph:
    if not j in visited:
        cnt = dfs(j)
        maxi = max(cnt, maxi)
 
print(maxi)