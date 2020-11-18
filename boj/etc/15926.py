n = int(input())
lst = list(input())

stk = [-1]

max_len = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stk.append(i)
    else:
        stk.pop()
        if stk:
            max_len = max(max_len, i - stk[-1])
        else:
            stk.append(i)

print(max_len)