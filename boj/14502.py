from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

wall = []

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            wall.append((i,j))

move_r = [0,0,-1,1]
move_c = [1,-1,0,0]

def bfs(row, col):
    q = deque()
    q.append((row,col))

    while q:
        cur_r, cur_c = q.popleft()

        for s in range(4):
            next_r = cur_r + move_r[s]
            next_c = cur_c + move_c[s]

            if 0 <= next_r < n and 0 <= next_c < m:
                if lst[next_r][next_c] == 0 and not (next_r, next_c) in walls and safe_area[next_r][next_c] == True:
                    safe_area[next_r][next_c] = False
                    q.append((next_r, next_c))

ans = 0

# search about each case (comb of walls) brute force
for walls in combinations(wall, 3):
    safe_area = [[True]*m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if lst[r][c] == 1 or (r,c) in walls:
                safe_area[r][c] = False

            elif lst[r][c] == 2 and safe_area[r][c] == True:
                safe_area[r][c] = False
                bfs(r,c)
    cnt = 0
    for line in safe_area:
        cnt += line.count(True)

    ans = max(ans, cnt)

print(ans)