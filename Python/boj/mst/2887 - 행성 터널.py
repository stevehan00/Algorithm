def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 != v2: parent[v2] = v1

def parentCk(v1, v2):
    v1 = find(v1)
    v2 = find(v2)
    if v1 == v2: return False
    else: return True

def sol():
    result = 0
    for w, v1, v2 in adj:
        if parentCk(v1, v2):
            union(v1, v2)
            result += w
    return result

N = int(input())
parent = [i for i in range(N)]
adj = []
planet = []

for i in range(N):
    x, y, z = map(int, input().split())
    planet.append([x, y, z, i])

for i in range(3):
    planet.sort(key=lambda x:x[i])
    before = planet[0][3]

    for j in range(1, N):
        current = planet[j][3]
        adj.append([abs(planet[j][i]-planet[j-1][i]), before, current])
        before = current

adj.sort()
print(sol())