n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

left, right = 1, max(lst)
ans = 0

while left <= right:
    mid = (left+right)//2

    cnt = 0
    for c in lst:
        if c < mid:
            cnt += mid - c
    
    if cnt > k:
        right = mid - 1
    else:
        left = mid + 1
        ans = mid

print(ans)