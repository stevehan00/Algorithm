import sys

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

start, end, sums, length = 0, 0, lst[0], 100001

while start < n:
    
    if sums > s or end == n-1:
        sums -= lst[start]
        start += 1
     
    else:
        end += 1
        sums += lst[end]

    if sums > s:
        print(start, end, sums) 
        length = min(length, end-start+1)

if length == 100001:
    length = 0

print(length)