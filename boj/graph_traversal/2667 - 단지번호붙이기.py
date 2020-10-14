import sys, heapq

n = int(sys.stdin.readline())
lst = [list(sys.stdin.readline()[:-1]) for _ in range(n)]

def dfs(r,c, count):
    lst[r][c] = 0

    mr = [1,-1,0,0]
    mc = [0,0,1,-1]

    for i in range(4):
        nr = r + mr[i]
        nc = c + mc[i]

        if nr >=0 and nc >= 0 and nr < n and nc < n:
            if lst[nr][nc] == '1':
                count = dfs(nr, nc, count + 1)
    
    return count


pq = []

for i in range(n):
    for j in range(n):
        if lst[i][j] == '1':
            sums = dfs(i,j, 1)
            heapq.heappush(pq, sums)

print(len(pq))
while pq:
    print(heapq.heappop(pq))