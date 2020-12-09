import sys

rank = {}
parent = {}

def find(nn):
    if parent[nn] != nn:
        parent[nn] = find(parent[nn])
    return parent[nn]

def union(n1,n2):
    r1 = find(n1)
    r2 = find(n2)

    if rank[r1] < rank[r2]:
        parent[r1] = r2
    else:
        parent[r2] = r1
        if rank[r1] == rank[r2]:
            rank[r1] += 1

def kruscal():
    s = 0
    c = 1
    for e in edges:
        d,u,v = e
        if find(u) != find(v) and gender[u] != gender[v]:
            union(u,v)
            s += d
            c += 1

    if c == n:
        return s
    else:
        return -1

n,m = map(int, sys.stdin.readline().split())
gender = [0] + list(input().split())

edges = []

for i in range(1,n+1):
    rank[i] = 0
    parent[i] = i

for _ in range(m):
    u,v,d = map(int, sys.stdin.readline().split())
    if gender[u] == gender[v]:
        continue
    edges.append((d,u,v))

edges.sort()
ans = kruscal()

print(ans)