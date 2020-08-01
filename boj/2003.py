n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end, cnt, sums = 0, 0, 0, 0

while start < n:
    if sums >= m or end == n:
        sums -= a[start]
        start += 1
    
    else:
        sums += a[end]
        end += 1

    if sums == m:
        cnt += 1

print(cnt)