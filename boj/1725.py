n = int(input())
stk = []
ipt = []

ans = 0

for i in range(n):
    
    s = int(input())
    ipt.append(s)
    
    while stk and ipt[stk[-1]] > s:
        h = ipt[stk.pop()]
        if stk:
            w = i - stk[-1] - 1
        else:
            w = i
        ans = max(ans, h*w)

    stk.append(i)

while stk:
    h = ipt[stk.pop()]
    if stk:
        w = i - stk[-1] - 1
    else:
        w = i
    ans = max(ans, h*w)
print(ans)