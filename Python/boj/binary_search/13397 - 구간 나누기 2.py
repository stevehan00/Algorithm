n, m = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 10000
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    maxs = lst[0]
    mins = lst[0]

    sums = 1

    for i in range(1, n):
        if lst[i] > maxs : maxs = lst[i]
        if lst[i] < mins : mins = lst[i]

        if maxs - mins > mid:
            sums += 1

            maxs = lst[i]
            mins = lst[i]
    
    if sums <= m:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
     
print(ans)