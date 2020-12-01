from collections import defaultdict
import sys

INF = sys.maxsize

n = int(input())

lst = [[]]

def search(node):
    if visit[node] == 1:
        return False
    
    visit[node] = 1

    for j in range(1,n+1):
        if adj[node][j] == 1:
            flag = search(val[j])
            if (val[j] == 0) or flag:
                val[j] = node
                return True

    return False

for _ in range(n):
    lst.append(list(map(int, input().split())))

adj = [[0]*(n+1) for _ in range(n+1)]
val = [0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        if lst[j][0] == lst[i][0] and lst[j][1] == lst[i][1] and lst[j][2] == lst[i][2] and i > j:
            continue
        if lst[j][0] <= lst[i][0] and lst[j][1] <= lst[i][1] and lst[j][2] <= lst[i][2]:
            adj[i][j] = 1
for _ in range(2):
    for i in range(1, n+1):
        visit = [0 for _ in range(n+1)]
        search(i)

print(val[1:].count(0))