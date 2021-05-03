import sys

input = sys.stdin.readline
n,m = map(int, input().rstrip().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

left = 1
right = m*max(lst)
ans = 0

while left <= right:
    half = (left+right) // 2

    cnt = 0
    for k in range(len(lst)):
        cnt += half // lst[k]
        if cnt >= m:
            break
    
    if cnt >= m:
        right = half - 1
        ans = half
    else:
        left = half + 1

print(ans)