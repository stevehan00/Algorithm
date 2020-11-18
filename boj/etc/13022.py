s = input()
idx_start = 0
idx_temp = 1

flag = True

while idx_start < len(s):
    if s[idx_start] == 'w':
        n = 0
        while idx_start < len(s) and s[idx_start] == 'w':
            n += 1
            idx_start += 1

        if idx_start+n*3 > len(s):
            flag = False
            break

        temp = 'o'*n + 'l'*n + 'f'*n
        
        if temp != s[idx_start:idx_start+3*n]:
            flag = False
            break
        else:
            idx_start = idx_start + n*3


    else:
        flag = False
        break


if flag:
    print(1)
else:
    print(0)