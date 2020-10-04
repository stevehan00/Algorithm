n, m = map(int ,input().split())
lst = list(map(int ,input().split()))
 
p = sum(lst)
 
if n < p:
    print(-1)
else:
    print(n-p)