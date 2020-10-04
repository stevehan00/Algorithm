n = int(input())
result = [0 for i in range(n)]
lst = list(map(int, input().split()))
 
for i in lst:
    result[i-1] += 1
 
for i in result:
    print(i)