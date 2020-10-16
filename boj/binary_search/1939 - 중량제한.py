import sys
from collections import defaultdict, deque

graph = defaultdict(list)
n, m = map(int, sys.stdin.readline().split())
right = 1
left = 1

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    right = max(right, c)

s, e = map(int, sys.stdin.readline().split())

def bfs(lim):
    dq = deque()
    dq.append(s)
    
    visit = set()
    visit.add(s)
    
    while dq:
        cur = dq.popleft()
        if cur == e:
            return True
        
        for c in graph[cur]:
            if not c[0] in visit and c[1] >= lim:
                visit.add(c[0])
                dq.append(c[0])

    return False

ans = 0
while left <= right:
    mid = (left + right) // 2

    flag = bfs(mid)

    if flag:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1


print(ans)