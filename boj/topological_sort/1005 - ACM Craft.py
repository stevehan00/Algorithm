from collections import deque
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n,k = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))

    inDegree = [0 for _ in range(n+1)]
    graph= [[] for _ in range(n+1)]

    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        inDegree[b] += 1
    
    target = int(sys.stdin.readline())

    q = deque()

    result = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            result[i] = time[i]


    while q:
        cur = q.popleft()

        for c in graph[cur]:
            inDegree[c] -= 1
            if result[c] == 0:
                result[c] = result[cur] + time[c]
            else:
                result[c] = max(result[c], result[cur]+time[c])
            if inDegree[c] == 0:
                q.append(c)
                
    print(result[target])