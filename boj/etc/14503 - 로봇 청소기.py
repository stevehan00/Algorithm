import sys

n,m = map(int, sys.stdin.readline().split())
robot = list(map(int, sys.stdin.readline().split()))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]

ans = 1
signal = 0
flag = True

visit[robot[0]][robot[1]] = True

while flag:
    sw = False
    for _ in range(4):
        robot[2] = (robot[2] + 3)%4

        next_r = robot[0] + dr[robot[2]]
        next_c = robot[1] + dc[robot[2]]

        if 0 <= next_r < n and 0 <= next_c < m:
            if visit[next_r][next_c] == False and lst[next_r][next_c] == 0:
                robot[0] = next_r
                robot[1] = next_c
                visit[next_r][next_c] = True
                ans += 1
                sw = True
                break
    
    if not sw:
        temp = (robot[2] + 2)%4 
        temp_r = robot[0]+dr[temp]
        temp_c = robot[1]+dc[temp]
        if 0 <= temp_r < n and 0 <= temp_c < m and lst[temp_r][temp_c] == 0:
            robot[0] = temp_r
            robot[1] = temp_c
        else:
            flag = False


print(ans)    