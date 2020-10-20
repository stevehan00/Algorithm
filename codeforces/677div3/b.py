t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    pre = -1
    for i in range(n):
        if lst[i] == 1:
            if pre == -1:
                pre = i
            else:
                ans += i-pre-1
                pre = i
    
    print(ans)
        