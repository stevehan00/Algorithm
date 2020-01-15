num = int(input())
lst = []
for i in range(num):
    k = int(input())
    if k==0:
        lst.pop()
    else:
        lst.append(k)

result = 0

if len(lst) >= 1:
    for i in lst:
        result += i
    print(result)
else:
    print('0')