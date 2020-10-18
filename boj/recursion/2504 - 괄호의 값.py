s = input()

stk = []
flag = True
ans = 0

for i in s:
    if i == '(' or i =='[':
        stk.append(i)
    else:
        if len(stk) == 0:
            flag = False
            break
            
        if i == ')':
            temp = 0
            if stk[-1] == '(':
                stk.pop()
                stk.append(2)
            else:
                while len(stk) > 0 and type(stk[-1]) == int:
                    temp += stk.pop()
                if len(stk) == 0:
                    flag = False
                    break
                if stk[-1] == '(':
                    stk.pop()
                    stk.append(temp*2)
                else:
                    flag = False
                    break
        if i == ']':
            temp = 0
            if stk[-1] == '[':
                stk.pop()
                stk.append(3)
            else:
                while len(stk) > 0 and type(stk[-1]) == int:
                    temp += stk.pop()
                if len(stk) == 0:
                    flag = False
                    break
                if stk[-1] == '[':
                    stk.pop()
                    stk.append(temp*3)
                else:
                    flag = False
                    break

for c in stk:
    if c == '(' or c =='[':
        flag = False
        break

if flag:
    print(sum(stk))
else:
    print(0)