import sys
from collections import deque

input = sys.stdin.readline

def index_decide(r,c):
    if 0<= r < n and 0 <= c < n:
        return True
    return False

n = int(input())
grid = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    a,b = map(int, input().split())
    grid[a-1][b-1] = 1

l = int(input())
arr = []
for _ in range(l):
    line = list(input().rstrip().split())
    arr.append((int(line[0]), line[1]))

grid[0][0] = -1

snake = deque()
snake.append((0,0))

cur_r = 0
cur_c = 0

tail_r = 0
tail_c = 0

time = 0

change = 0
arrow = ['R','D','L','U']
arrow_idx = 0

while True:
    time += 1
    if arrow[arrow_idx]=='R':
        next_r = cur_r
        next_c = cur_c + 1
    elif arrow[arrow_idx]=='L':
        next_r = cur_r
        next_c = cur_c - 1
    elif arrow[arrow_idx]=='U':
        next_r = cur_r-1
        next_c = cur_c
    else:
        next_r = cur_r+1
        next_c = cur_c
    
    if not index_decide(next_r, next_c):
        break

    if grid[next_r][next_c] == -1:
        break
    elif grid[next_r][next_c] == 0:
        grid[next_r][next_c] = -1
        tail_r, tail_c = snake.popleft()
        grid[tail_r][tail_c] = 0

    snake.append((next_r, next_c))
    grid[next_r][next_c] = -1
    cur_r = next_r
    cur_c = next_c

    if change < l and time == arr[change][0]:
        if arr[change][1] == 'D':
            arrow_idx = (arrow_idx+1)%4
        else:
            arrow_idx = (arrow_idx-1+4)%4
        change += 1

print(time)