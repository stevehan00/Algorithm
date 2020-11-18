n, k = map(int ,input().split())

lst = [i for i in range(1, n+1)]

temp = []
i = k-1
while(True):
    temp.append(lst.pop(i))
    if not lst:
        break
    i = (i+k-1)%len(lst)

print('<'+', '.join(map(str, temp))+'>')