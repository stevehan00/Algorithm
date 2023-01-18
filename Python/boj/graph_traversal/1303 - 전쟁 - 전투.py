c, r = map(int, input().split())
lst = [list(input()) for _ in range(r)]

move_r = [0, 0, 1, -1]
move_c = [1, -1, 0, 0]

def dfs(ch ,ro,co):
    stk = [(ro,co)]
    visited[ro][co] = True
    cnt = 0
    while stk:
        cur_r, cur_c = stk.pop()

        for k in range(4):
            next_r = cur_r + move_r[k]
            next_c = cur_c + move_c[k]

            if 0 <= next_r < r and 0 <= next_c < c:
                if visited[next_r][next_c] == False and lst[next_r][next_c] == ch:
                    visited[next_r][next_c] = True
                    stk.append((next_r, next_c))
                    cnt += 1

    return cnt

w_cnt = 0
b_cnt = 0

visited = [[False]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if visited[i][j] == False:
            if lst[i][j] == 'W':
                w_cnt += (dfs('W',i,j) + 1)**2

            else:
                b_cnt += (dfs('B',i,j) + 1)**2

print(w_cnt, b_cnt)