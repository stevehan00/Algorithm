from math import gcd

n = int(input())

top = []
bot = []

for _ in range(n):
    a,b = map(int, input().split())
    p = gcd(a,b)
    if gcd(a,b) != 1:
        a = a//p
        b = b//p

    top.append(a)
    bot.append(b)


gg = top[0]

for c in top[1:]:
    gg = gcd(gg, c)

hh = bot[0]

for c in bot[1:]:
    hh = c*hh//gcd(c,hh)


temp = gcd(gg,hh)
print(gg//temp, hh//temp)