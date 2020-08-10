n = int(input())
stk = []

cnt = 0

for _ in range(n):
    num = int(input())
    
    if len(stk) == 0:
        stk.append(num)
    else:
        if stk[-1] > num:
            cnt += len(stk)
            stk.append(num)
            
        else:
            while stk and stk[-1] <= num:
                stk.pop()

            cnt += len(stk)
            stk.append(num)


print(cnt)
