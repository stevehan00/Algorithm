import sys

input =  sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = []

    for _ in range(n):
        a,b = map(int, input().split())
        lst.append((a,b))

    lst.sort()

    ans = 1
    second = lst[0][1]

    for c in lst[1:]:
        if c[1] < second:
            second = c[1]
            ans += 1
    
    print(ans)