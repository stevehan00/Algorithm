import copy
from collections import deque

r,c = map(int, input().split()) 
arr = []

d= None
s = None
stars = deque()

for i in range(r):
    line = list(input())

    for j in range(c):
        if line[j] == '*':
            stars.append((i,j))
        elif line[j] == 'S':
            s = (i,j)
        elif line[j] == 'D':
            d = (i,j)
    
    arr.append(line)

q = deque()
q.append(s)

flag = False
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while q:
    
    if flag:
        break

    if stars:
        ll = len(stars)
        for _ in range(ll):
            xx,yy = stars.popleft()

            for t in range(4):
                nxx = xx + dx[t]
                nyy = yy + dy[t]

                if 0 <= nxx < r and 0 <= nyy < c and (arr[nxx][nyy] == '.' or arr[nxx][nyy] == 'S'):
                    arr[nxx][nyy] = '*'
                    stars.append((nxx,nyy))
    ll = len(q)
    for t in range(ll):
        if flag:
            break

        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]

            if d[0] == nx and d[1] == ny:
                flag = True
                break

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                arr[nx][ny] = 'S'
                q.append((nx,ny))

    cnt += 1

if flag:
    print(cnt)
else:
    print('KAKTUS')