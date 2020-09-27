from collections import deque
import sys, heapq

m,n,p = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline())[:-1] for _ in range(m)]

pp = dict()
for _ in range(p):
    a,b = sys.stdin.readline().split()
    pp[a] = int(b)

b_hp = int(sys.stdin.readline())

def bfs(row, col):
    stk = []
    stk.append((0, row, col))

    te = [[sys.maxsize]*(n) for _ in range(m)]

    while stk:
        tt, cur_r, cur_c = heapq.heappop(stk)


        if (0<= cur_r+1 < m) and tt+1 < te[cur_r+1][cur_c]:
            if lst[cur_r+1][cur_c] == 'B':
                return tt+1
            if lst[cur_r+1][cur_c] == '.' or (97 <= ord(lst[i][j]) <= 122):
                te[cur_r+1][cur_c] = tt+1
                heapq.heappush(stk, (tt+1, cur_r+1, cur_c))

        if (0<= cur_c+1 < n) and tt+1 < te[cur_r][cur_c+1]:
            if lst[cur_r][cur_c+1] == 'B':
                return tt+1
            if lst[cur_r][cur_c+1] == '.' or (97 <= ord(lst[i][j]) <= 122):
                te[cur_r][cur_c+1] = tt+1
                heapq.heappush(stk, (tt+1, cur_r, cur_c+1))

        if (0<= cur_r-1 < m) and tt+1 < te[cur_r-1][cur_c]:
            if lst[cur_r-1][cur_c] == 'B':
                return tt+1
            if lst[cur_r-1][cur_c] == '.' or (97 <= ord(lst[i][j]) <= 122):
                te[cur_r-1][cur_c] = tt+1
                heapq.heappush(stk, (tt+1, cur_r-1, cur_c))

        if (0<= cur_c-1 < n) and tt+1 < te[cur_r][cur_c-1]:
            if lst[cur_r][cur_c-1] == 'B':
                return tt+1
            if lst[cur_r][cur_c-1] == '.' or (97 <= ord(lst[i][j]) <= 122):
                te[cur_r][cur_c-1] = tt+1
                heapq.heappush(stk, (tt+1, cur_r, cur_c-1))
            

g = []

for i in range(m):
    for j in range(n):
        if 97 <= ord(lst[i][j]) <= 122:
            tar = lst[i][j]
            g.append((bfs(i,j), tar))
            
            if len(g) == p:
                break

heapq.heapify(g)

cnt = 0
acc = 0

while b_hp > 0:
    cnt += 1
    time, num = heapq.heappop(g)
    acc += pp[num]
    if not g:
        break
    dis = g[0][0] - time

    b_hp -= dis*acc

print(cnt)
