import sys

s = input()

stk = []

while True:
    ipt = input()
    if ipt == '고무오리 디버깅 끝':
        break

    if stk and ipt == '고무오리':
        stk.pop()
    
    elif not stk and ipt == '고무오리':
        stk.append(1)
        stk.append(1)
    
    if ipt == '문제':
        stk.append(1)


if stk:
    print('힝구')
else:
    print('고무오리야 사랑해')