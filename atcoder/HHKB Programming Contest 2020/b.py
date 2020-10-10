h, w = map(int, input().split())

lst = [list(input()) for _ in range(h)]
cnt = 0

for i in range(h):
    for j in range(w):
        if lst[i][j] == '#':
            continue
        if 0 <= i-1 and lst[i-1][j] == '.':
            cnt += 1
        if 0 <= j-1 and lst[i][j-1] == '.':
            cnt += 1
        if i+1 < h and lst[i+1][j] == '.':
            cnt += 1
        if j+1 < w and lst[i][j+1] == '.':
            cnt += 1

print(cnt//2)