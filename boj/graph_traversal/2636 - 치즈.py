import sys, copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def adj(r,c):
    for k in range(4):
        nr = r + dx[k]
        nc = c + dy[k]

        if 0 <= nr < n and 0 <= nc < m:
            if lst[nr][nc] == 0:
                return True
    
    return False

def zero():
    for i in range(n):
        for j in range(m):
            if lst[i][j] != 0:
                return False
    
    return True

n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

time = 0
cnt = 0

while True:
    for c in lst:
        print(c)
    print()
    if zero():
        print(time)
        print(cnt)
        break

    t = copy.deepcopy(lst)
    temp = 0

    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                temp += 1
            if adj(i,j):
                t[i][j] = 0

    time += 1
    
    cnt = temp
    lst = copy.deepcopy(t)