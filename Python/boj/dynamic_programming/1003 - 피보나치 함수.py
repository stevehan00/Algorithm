t = int(input())

cnt_z =[0]*41
cnt_z[0] = 1
cnt_z[1] = 0

cnt_o = [0]*41
cnt_o[0] = 0
cnt_o[1] = 1

for _ in range(t):
    n = int(input())

    if n < 2:
        print(cnt_z[n], cnt_o[n])
    else:
        for i in range(2, n+1):
            cnt_z[i] = cnt_z[i-1] + cnt_z[i-2]
            cnt_o[i] = cnt_o[i-1] + cnt_o[i-2]

        print(cnt_z[n], cnt_o[n])