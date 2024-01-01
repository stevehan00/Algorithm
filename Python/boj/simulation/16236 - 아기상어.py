n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

mv_r = (-1,0,0,1)
mv_c = (0,-1,1,0)

def search(i,j):
    cand = []
    dist[i][j] = 1
    que = [(i,j)]

    while que:
        cur = que.pop(0)

        for i in range(4):
            nex_r = cur[0] + mv_r[i]
            nex_c = cur[1] + mv_c[i]

            if 0 <= nex_r < n and 0 <= nex_c < n:
                if dist[nex_r][nex_c] != 0:
                    continue

                if board[nex_r][nex_c] == 0 or board[nex_r][nex_c] == size:
                    dist[nex_r][nex_c] = dist[cur[0]][cur[1]]+1
                    que.append((nex_r, nex_c))
                else:
                    if board[nex_r][nex_c] < size:
                        dist[nex_r][nex_c] = dist[cur[0]][cur[1]]+1
                        cand.append((nex_r,nex_c, dist[cur[0]][cur[1]]+1))

    return cand

size = 2
ate = 0
pos = [0,0]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            pos[0] = i
            pos[1] = j
ans = 0

while True:
    dist = [[0]*n for _ in range(n)]
    cand = search(pos[0], pos[1])
    if len(cand) == 0:
        break
    cand.sort(key=lambda x: (x[2], x[0], x[1]))
    fish_r, fish_c, fish_d = cand[0]

    ate += 1
    if ate == size:
        size += 1
        ate = 0
    
    board[fish_r][fish_c] = 9
    board[pos[0]][pos[1]] = 0
    pos[0], pos[1] = fish_r, fish_c

    ans += fish_d - 1

print(ans)