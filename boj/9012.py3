num = int(input())

for _ in range(num):
    l = 1
    stack = []
    s = input().rstrip()
    for i in range(len(s)):
        if s[i] =='(':
            stack.append(1)
        elif s[i]==')':
            if len(stack) == 0:
                l = 0
                break
            else:
                stack.pop()
        
    if len(stack) != 0:
        l = 0
    
    if l == 1:
        print('YES')
    else:
        print('NO')