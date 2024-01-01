lst = list(map(int, input().split()))

ab = (lst[2]-lst[0], lst[3]-lst[1])
ad = (lst[6]-lst[0], lst[7]-lst[1])
ac = (lst[4]-lst[0], lst[5]-lst[1])
fi = ab[0]*ad[1] - ab[1]*ad[0]
se = ab[0]*ac[1] - ab[1]*ac[0]

if fi*se >= 0:
    print(0)
else:
    print(1)