import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m,k = map(int, input().split())
grid = [[0]*m for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    grid[a-1][b-1] = 1

def dfs(r,c,cnt):
    if (r < 0 or r >= n) or (c < 0 or c >= m):
        return cnt-1

    if grid[r][c] == 0:
        return cnt-1
        
    grid[r][c] = 0

    re1 = dfs(r-1,c,cnt+1)
    re2 = dfs(r,c-1,re1+1)
    re3 = dfs(r+1,c,re2+1)
    re4 = dfs(r,c+1,re3+1)

    return re4

cnt = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            c = dfs(i,j, 1)
            cnt = max(cnt, c)

print(cnt)