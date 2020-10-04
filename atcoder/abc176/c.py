n = int(input())
lst = list(map(int, input().split()))
cnt = 0 
for i in range(1, n):
    if lst[i-1] > lst[i]:
        cnt += lst[i-1] - lst[i]
        lst[i] = lst[i-1]
 
print(cnt)