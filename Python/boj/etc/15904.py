lst = input()
res = []
for c in lst:

    if c == 'U' and len(res)==0:
        res.append('U')
    elif c == 'C' and len(res)==1:
        res.append('C')
    elif c == 'P' and len(res)==2:
        res.append('P')
    elif c == 'C' and len(res)==3:
        res.append('C')

    if res[:] == ['U','C','P','C']:
        print('I love UCPC')
        exit()

print('I hate UCPC')