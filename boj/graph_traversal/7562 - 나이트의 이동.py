from collections import deque

t = int(input())

mv_r = [1,2,1,2,-1,-2,-1,-2]
mv_c = [2,1,-2,-1,2,1,-2,-1]

for _ in range(t):
    n = int(input())
    sr, sc = map(int ,input().split())
    er, ec = map(int ,input().split())

    visited = [[0]*n for _ in range(n)]

    dq = deque()
    dq.append((sr,sc))
    visited[sr][sc] = 0
    cnt = 0
    while dq:
        cur = dq.popleft()

        if cur[0] == er and cur[1] == ec:
            break

        for i in range(8):
            nr = cur[0] + mv_r[i]
            nc = cur[1] + mv_c[i]


            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                visited[nr][nc] = visited[cur[0]][cur[1]] + 1
                dq.append((nr,nc))

                if nr == er and nc == ec:
                    break

    print(visited[er][ec])