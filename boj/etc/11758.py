x = [0,0,0]
y = [0,0,0]
for i in range(3):
    x[i], y[i] = map(int, input().split())
k=x[0]*y[1]+x[1]*y[2]+x[2]*y[0]-(x[1]*y[0]+x[2]*y[1]+x[0]*y[2])
if k>0:
    print('1')
elif k<0:
    print('-1')
else:
    print('0')