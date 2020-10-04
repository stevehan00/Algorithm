import sys
 
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
 
result = lst[n//2:]
 
for i in range(n//2):
    result.insert(2*i + 1, lst[i])
 
cnt = 0
for i in range(1, n - 1):
    if result[i - 1] > result[i] and result[i] < result[i + 1]:
        cnt += 1
 
print(cnt)
print(' '.join(map(str,result)))