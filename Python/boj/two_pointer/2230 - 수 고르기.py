n, m = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()

l, r = 0, 1
ans = lst[len(lst)-1] - lst[l]

if m == 0:
    print(0)
    exit()

while l != n:
    temp = lst[r] - lst[l]

    if r == n-1:
        l += 1

    elif temp > m:
        l += 1
    elif temp < m:
        r += 1
    
    if temp == m:
        ans = temp
        break
    
    if ans > temp >= m:
        ans = temp
    

print(ans)