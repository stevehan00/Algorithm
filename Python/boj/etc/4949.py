while True:
    stk = []
    s = input()

    result = True

    if s==".":
        break
    
    for i in s:
        if (i == "(") or (i == "["):
            stk.append(i)
        elif i==")":
            if len(stk) == 0:
                result = False
                break
            if stk[-1] == "(":
                stk.pop()
            else:
                result = False
                break
        elif i=="]":
            if len(stk) == 0:
                result = False
                break
            if stk[-1] == "[":
                stk.pop()
            else:
                result = False
                break

    if len(stk):
        result = False
    
    if result:
        print("yes")
    else:
        print("no")
