n=int(input())
day=0

while n!=0:
    day+=1
    l = []

    t = [0]*25

    for _ in range(n):
        l.append(list(map(int, input().split())))

    l.sort(key=lambda x: x[1]-x[0])

    for line in l:
        for i in range(line[0],line[1]):
            if t[i] == 2:
                continue
            else:
                t[i]+=1
                break

    print('On day',day,'Emma can attend as many as',sum(t),'parties.')

    n=int(input())