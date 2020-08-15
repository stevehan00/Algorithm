n = int(input())
day = 1
aaa = []

while n != 0:
    lst = []
    ans = 0

    for  i in range(n):
        s, e = map(int, input().split())
        lst.append((s, e))
    
    lst.sort(key=lambda x : (x[0], x[1]))
    
    cur_t, cur_m = 0, 0
    for i in range(n):
        if i == 0:
            cur_t = lst[i][0]
            cur_m += 30
            ans += 1
        else:
            if cur_t >= lst[i][1]:
                continue

            if cur_t >= lst[i][0]:
                if cur_m == 0:
                    cur_m += 30
                else:
                    cur_t += 1
                    cur_m = 0
                ans += 1
            else:
                cur_t = lst[i][0]
                cur_m = 30
                ans += 1

    aaa.append((day, ans))
    # print("On day",day,"Emma can attend as many as",ans,"parties.")
    day += 1
    n = int(input())


for i in aaa:
    print(i)