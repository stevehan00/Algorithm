t = int(input())
 
for _ in range(t):
    n,m = map(int, input().split())
    tiles = []
    for _ in range(n):
        temp = []
        temp.append(list(map(int, input().split())))
        temp.append(list(map(int, input().split())))
        tiles.append(temp)
    
    if m*m % 2 == 1:
        print('NO')
        continue
 
    c = False
 
    for v in range(n):
        if tiles[v][0][1] == tiles[v][1][0]:
            c = True
            break
    
    if c:
        print('YES')
    else:
        print('NO')