a,b,c,d = map(int, input().split())
ac = a*c
ad = a*d
bc = b*c
bd = b*d
print(max(bd, ac, ad, bc))