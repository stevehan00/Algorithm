import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split(' '))
parent = [i for i in range(n+1)]
cnt = 0

for i in range(m):
    a,b = map(int, input().split(' '))
    if find(parent,a) == find(parent,b):
        cnt = i+1
        break
    else:
        union(parent, a, b)

print(cnt)