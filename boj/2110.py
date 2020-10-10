n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
ans = 0

left, right = 1, lst[-1] - lst[0]

while left <= right:
    mid = (left + right) // 2
    
    cnt = 1
    cur_h = lst[0]
    for s in lst[1:]:
        if s - cur_h >= mid:
            cnt += 1
            cur_h = s
        
        if cnt >= c:
            break
    
    if cnt >= c:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)