k,n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

left, right = 1, max(lst)
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for c in lst:
        cnt += c // mid

        if cnt >= n:
            break
    
    if cnt >= n:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1


print(ans)