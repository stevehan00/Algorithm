import sys

r, c = map(int, sys.stdin.readline().split())
lst = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

move_r = [0, 0, -1, 1]
move_c = [1, -1, 0, 0]

def dfs(row, col):
    stk = [(row, col)]
    visited[row][col] = True

    o = 0
    v = 0

    while stk:
        cur_r, cur_c = stk.pop()
        
        for i in range(4):
            next_r = cur_r + move_r[i]
            next_c = cur_c + move_c[i]

            if (0<= next_r < r and 0<= next_c < c) and visited[next_r][next_c] == False:
                if lst[next_r][next_c] == 'o':
                    o += 1
                elif lst[next_r][next_c] == 'v':
                    v += 1
                elif lst[next_r][next_c] == '#':
                    continue
                
                visited[next_r][next_c] = True
                stk.append((next_r, next_c))

    return o, v




o_cnt = 0
v_cnt = 0

for i in range(r):
    for j in range(c):
        o_temp = 0
        v_temp = 0

        if visited[i][j] == False:
            if lst[i][j] == 'o':
                tt = dfs(i, j)
                o_temp += tt[0] + 1
                v_temp += tt[1]

            elif lst[i][j] == 'v':
                tt = dfs(i, j)
                o_temp += tt[0]
                v_temp += tt[1] + 1

            if o_temp > v_temp:
                o_cnt += o_temp
            else:
                v_cnt += v_temp


print(o_cnt, v_cnt)