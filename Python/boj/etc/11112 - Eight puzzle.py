import sys
t = int(sys.stdin.readline())

### Time Limit ###

goal = [[1,2,3], [4,5,6], [7,8,0]]

ans = []

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def isSolvable():
    inv_cnt = 0

    for i in range(8):
        for j in range(i+1, 9):
            f_row = i//3
            f_col = i%3
            s_row = j//3
            s_col = j%3

            if (cur[f_row][f_col] != 0 and cur[s_row][s_col] != 0) and (cur[f_row][f_col] > cur[s_row][s_col]):
                inv_cnt += 1

    return inv_cnt % 2 == 0

def h():
    temp = 0
    for i in range(3):
        for j in range(3):
            if cur[i][j] != goal[i][j]:
                temp += 1
    
    return temp


for _ in range(t):
    sys.stdin.readline()
    
    cur = []
    start = [0,0]

    for i in range(3):
        line = list(sys.stdin.readline()[:-1])
        for j in range(3):
            if line[j] != '#':
                line[j] = int(line[j])
            else:
                start[0] = i
                start[1] = j
                line[j] = 0

        cur.append(line)

    if not isSolvable():
        ans.append('impossible')
    else:
        cnt = 0
        flag = True

        for i in range(3):
            for j in range(3):
                if cur[i][j] != goal[i][j]:
                    flag = False
                    break
        if flag:
            ans.append(0)
            continue

        while True:
            mins = [start[0],start[1],sys.maxsize]

            for i in range(4):
                nr = mins[0] + dr[i]
                nc = mins[1] + dc[i]
                
                if 0 <= nr < 3 and 0 <= nc < 3:

                    cur[nr][nc], cur[start[0]][start[1]] = cur[start[0]][start[1]], cur[nr][nc]

                    temp = h()

                    cur[start[0]][start[1]], cur[nr][nc] = cur[nr][nc], cur[start[0]][start[1]]
                    
                    if temp < mins[2]:
                        mins[0] = nr
                        mins[1] = nc
                        mins[2] = temp

            cnt += 1

            cur[start[0]][start[1]], cur[mins[0]][mins[1]] = cur[mins[0]][mins[1]], cur[start[0]][start[1]]

            start[0] = mins[0]
            start[1] = mins[1]

            if mins[2] == 0:
                ans.append(cnt)
                break

for d in ans:
    print(d)