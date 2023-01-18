n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

if n == 1 and m == 1:
    print(1)
    exit()

move_r = [0,0,-1,1]
move_c = [1,-1,0,0]

ans = -1

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
q = [(0,0,False)]

while q:
    r, c, w = q.pop()

    for i in range(4):
        next_r = r + move_r[i]
        next_c = c + move_c[i]

        if next_r == n-1 and next_c == m-1:
            ans = visited[r][c] + 1
            break

        if 0 <= next_r < n and 0 <= next_c < m and visited[next_r][next_c] == 0:

            if lst[next_r][next_c] == '0':
                q.append((next_r,next_c, w))
                visited[next_r][next_c] = visited[r][c] + 1

            elif lst[next_r][next_c] == '1' and w == False:
                print(next_r, next_c)
                q.append((next_r, next_c, True))
                visited[next_r][next_c] = visited[r][c] + 1

    if ans != -1:
        break

print(ans)