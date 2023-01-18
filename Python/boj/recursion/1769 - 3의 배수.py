n = input()

def rec(n, cnt):
    if len(n) == 1:
        print(cnt)
        if n in ['3','6','9']:
            return True
        else:
            return False
    
    else:
        sums = 0
        for c in n:
            sums += int(c)
        
        return rec(str(sums), cnt+1)

if rec(n, 0):
    print('YES')
else:
    print('NO')