n = int(input())
c = list(input())
 
if 'R' not in c or 'W' not in c:
    print(0)
    exit()
 
left, right = 0, len(c) - 1
cnt = 0
 
while left < right:
 
    if c[left] == c[right] == 'W':
        right -= 1
        continue
 
    elif c[right] == c[left] == 'R':
        left += 1
        continue
 
    elif c[left+1] == 'R' and c[left] == 'W':
        c[left] = 'R'
        left += 1
 
    elif  c[right-1] == 'W' and c[right] == 'R':
        c[right] = 'W'
        right -= 1
 
    elif c[left] is 'W' and c[right] is 'R':
        c[left] = 'R'
        c[right] = 'W'
 
    else:
        left += 1
        right -= 1
        continue
 
    left += 1
    right -= 1
 
    cnt += 1
 
print(cnt) 