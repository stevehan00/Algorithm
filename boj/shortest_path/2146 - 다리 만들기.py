import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c,num):
    vis = [[0]*n for _ in range(n)]
    vis[r][c] = 1
    grid[r][c] = num
    q = deque()
    q.append((r,c))

    while q:
        cur = q.popleft()

        for k in range(4):
            n_r = cur[0] + dr[k]
            n_c = cur[1] + dc[k]

            if 0 <= n_r < n and 0 <= n_c < n and vis[n_r][n_c] == 0:
                if grid[n_r][n_c] == 1:
                    q.append((n_r, n_c))
                    vis[n_r][n_c] = 1
                    grid[n_r][n_c] = num

def bfs2(r,c,start):
    vis = [[0]*n for _ in range(n)]
    vis[r][c] = 1
    q = deque()
    q.append((r,c))

    while q:
        cur = q.popleft()
        cur_vis = vis[cur[0]][cur[1]]
        for k in range(4):
            n_r = cur[0] + dr[k]
            n_c = cur[1] + dc[k]
            if 0 <= n_r < n and 0 <= n_c < n and vis[n_r][n_c] == 0:
                if grid[n_r][n_c] == 0:
                    vis[n_r][n_c] = cur_vis + 1
                    q.append((n_r,n_c))
                else:
                    t = grid[n_r][n_c]
                    if t != 0 and t != start:
                        return cur_vis-1
    return sys.maxsize

cnt = 2
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bfs(i,j,cnt)
            cnt += 1

ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            val = bfs2(i,j,grid[i][j])
            ans = min(ans, val)

print(ans)