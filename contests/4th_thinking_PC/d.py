a = int(input())
lst = []

for i in range(1, a+1):
    c = 30
    while c > 0:
        c -= i+1
    
    if c+i+1 > i:
        lst.append(i)

for c in lst:
    print(c)