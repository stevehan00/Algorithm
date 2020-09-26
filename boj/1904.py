n = int(input())

p = 1
c = 2
t = 0

for i in range(n):
    t = p
    p = c
    c = (p+t)%15746

print(t)