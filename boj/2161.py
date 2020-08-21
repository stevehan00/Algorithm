from collections import deque

n = int(input())
lst = deque()

for i in range(1, n+1):
    lst.append(i)

ans = []

while len(lst) > 2:
    ans.append(lst.popleft())
    lst.append(lst.popleft())
ans += list(lst)
print(*ans)