from collections import defaultdict
import sys

parent = {}
rank = {}

def find(nn):
    if parent[nn] != nn:
        parent[nn] = find(parent[nn])

    return parent[nn]

def union(n1,n2):
    root1 = find(n1)
    root2 = find(n2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruscal():
    mst = []
    edges.sort()

    for e in edges:
        w,u,v = e

        if find(u) != find(v):
            union(u,v)
            mst.append(e)
    return mst

while True:
    m,n = map(int, sys.stdin.readline().split())
    edges = []

    if m == n == 0:
        break

    for i in range(m):
        parent[str(i)] = str(i)
        rank[str(i)] = 0

    total = 0

    for _ in range(n): 
        u,v,w = map(int, sys.stdin.readline().split())
        total += w
        edges.append((w,str(u),str(v)))

    b = kruscal()

    ans = 0

    for i in b:
        ans += i[0]

    print(total - ans)