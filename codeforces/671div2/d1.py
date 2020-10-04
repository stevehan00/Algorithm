import sys
 
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
 
lst.sort()
 
maxi = lst[n//2:]
result = []
 
for i in range(n//2):
    result.append(maxi[-i-1])
    result.append(lst[i])
 
if n % 2 != 0:
    result.append(maxi[0])
 
print((n-1)//2)
print(*result)