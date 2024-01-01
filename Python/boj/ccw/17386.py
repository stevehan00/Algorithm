x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())

ab = (x2-x1, y2-y1)
ac = (x3-x1, y3-y1)
ad = (x4-x1, y4-y1)

cd = (x4-x3, y4-y3)
cb = (x2-x3, y2-y3)
ca = (x1-x3, y1-y3)

fi = ab[0]*ac[1] - ab[1]*ac[0]
se = ab[0]*ad[1] - ab[1]*ad[0]

th = cd[0]*cb[1] - cd[1]*cb[0]
fo = cd[0]*ca[1] - cd[1]*ca[0]

if fi*se < 0 and th*fo < 0:
    print(1)
else:
    print(0)