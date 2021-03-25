import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

ans = 0
idx = 0

while idx < n-1 and lst[idx] <= 0:
    temp = lst[idx] * lst[idx+1]

    if temp < 0:
        ans += lst[idx]
        idx += 1
        break
    elif temp > 0:
        ans += temp
        idx += 2
    else:
        if lst[idx] == 0:
            idx += 1
        else:
            idx += 2

if idx == n-1 and lst[idx] < 0:
    ans += lst[idx]
else:
    idx = n-1

while idx > 0 and lst[idx] > 0:
    temp = lst[idx] * lst[idx-1]

    if temp <= 0:
        ans += lst[idx]
        break
    else:
        if lst[idx] == 1 or lst[idx-1] == 1:
            ans += lst[idx]
            idx -= 1
        else:
            ans += temp
            idx -= 2

if idx == 0 and lst[idx] > 0:
    ans += lst[idx]

print(ans)
