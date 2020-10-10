n = int(input())
lst = list(map(int, input().split()))

t = [0 for _ in range(200001)]
pre = 0

for c in lst:
    t[c] = 1

    for i in range(pre, len(t)):
        if t[i] == 0:
            print(i)
            pre = i
            break