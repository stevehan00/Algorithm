def check(a):
    for i in range(len(a)):
        b = ['F','F']
        for j in range(i+1, len(a)):
            if a[i] == a[j] and b[0] =='T':
                b[1] = 'T'
            if a[i] != a[j]:
                b[0] = 'T'
            if b[0] == 'T' and b[1] == 'T':
                return 0
    return 1

num = int(input())
res = 0
for i in range(num):
    a = input()
    res += check(a)
print(res)