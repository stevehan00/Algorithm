n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()

ans = 0

for i in range(n):
    num = n-i
    ans = max(ans, num*lst[i])

print(ans)