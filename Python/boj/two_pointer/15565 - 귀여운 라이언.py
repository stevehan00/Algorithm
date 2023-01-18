import sys

n, k = map(int, input().split())
lst = list(map(int, input().split()))

start, end, sums = 0, 0, 0
ans = sys.maxsize

if lst[0] == 1:
    sums += 1

while start < n:
    if sums >= k:
        ans = min(ans, end-start+1)

    if sums < k and end < len(lst)-1:
        end += 1
        if lst[end] == 1:
            sums += 1
    
    else:
        if lst[start] == 1:
            sums -= 1
        start += 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)