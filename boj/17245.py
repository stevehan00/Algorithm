n = int(input())
lst = []
left = 0
right = 0

sums = 0

for _ in range(n):
    line = list(map(int, input().split()))
    sums += sum(line)
    lst.append(line)
    right = max(right, max(line))

right += 1

sums = sums / 2
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for c in lst:
        for i in c:
            if i <= mid:
                cnt += i
            else:
                cnt += mid
        if cnt >= sums:
            break

    if cnt >= sums:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
    
print(ans)