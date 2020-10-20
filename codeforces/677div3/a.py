n = int(input())

lst = [0,1,3,6,10]

for _ in range(n):
    s = input()
    ans = 0
    leng = len(s)

    dig = int(s[0])
    ans += dig*10 - 10
    ans += lst[leng]

    print(ans)