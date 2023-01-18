import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(m)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c):
    visited = [[0]*n for _ in range(m)]
    visited[r][c] = 1
    result = 1
    q = deque()
    q.append((r,c))

    while q:
        cur = q.popleft()

        for k in range(4):
            next_r = cur[0] + dr[k]
            next_c = cur[1] + dc[k]

            if 0 <= next_r < m and 0 <= next_c < n and visited[next_r][next_c] == 0:
                if grid[next_r][next_c] == 'L':
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = visited[cur[0]][cur[1]] + 1

                    result = max(result, visited[next_r][next_c])

    return result - 1

ans = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == 'L':
            val = bfs(i,j)
            ans = max(ans, val)

print(ans)