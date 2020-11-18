import sys

origin = input()
subs = input()

subs_len = len(subs)

stk = []

for c in origin:
    stk.append(c)
    flag = True
    if len(stk) >= subs_len:
        for i in range(1, subs_len+1):
            if stk[-i] != subs[-i]:
                flag = False
                break
        
    if flag:
        for _ in range(subs_len):
            stk.pop()
    

if stk:
    print(''.join(map(str, stk)))
else:
    print('FRULA')