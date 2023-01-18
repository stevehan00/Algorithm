n = int(input())
lst = list(map(int, input().split()))


pre = lst[0]


for c in lst[1:]:
    pre = pre^c
if n == 1 and lst[0] == 1:
    print('cubelover')
    exit()
if pre == 0:
    print('koosaga')
else:
    print('cubelover')