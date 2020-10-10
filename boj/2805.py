n, m = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, max(lst)
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for c in lst:
        if c >= mid:
            cnt += c - mid
        if cnt >= m:
            break
    
    if cnt >= m:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)