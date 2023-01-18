from collections import deque
import sys, copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(r, c):
    q = deque()
    q.append((r,c))

    while q:
        cur = q.popleft()

        for k in range(4):
            nr = cur[0] + dx[k]
            nc = cur[1] + dy[k]

            if (0 <= nr < n and 0 <= nc < m) and t[nr][nc] != 0:
                q.append((nr,nc))
                t[nr][nc] = 0
                
def zero():
    for i in range(n):
        for j in range(m):
            if lst[i][j] != 0:
                return False
    return True

def adj_counter(r,c):
    counter = 0

    for k in range(4):
        nr = r + dx[k]
        nc = c + dy[k]

        if (0 <= nr < n and 0 <= nc < m) and t[nr][nc] == 0:
            counter += 1
    return counter

n,m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0

while True:
    if zero():
        print(0)
        break

    t = copy.deepcopy(lst)

    for i in range(n):
        for j in range(m):
            if lst[i][j] != 0:
                temp = lst[i][j] - adj_counter(i,j)
                temp = temp if temp > 0 else 0
                lst[i][j] = temp
    ans += 1
    t = copy.deepcopy(lst)
    cnt = 0

    for i in range(n):
        for j in range(m):
            if t[i][j] != 0:
                t[i][j] = 0
                bfs(i,j)
                cnt += 1
    if cnt > 1:
        print(ans)
        break