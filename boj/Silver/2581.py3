m = int(input())
n = int(input())
lst = []
sum = 0

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i%j==0:
            break
    else:
        lst.append(i)

if not lst:
    print('-1')
else:
    for i in lst:
         sum += i
    print(sum)
    print(lst[0])