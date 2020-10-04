t = int(input())
 
for _ in range(t):
    n = int(input())
    k = int(input())
    if n == 1:
        if k%2==0:
            print(2)
        else:
            print(1)
    else:
        if n % 2 == 0:
            lst = list(str(k))
            ans = False
            for c in range(1, n, 2):
                if int(lst[c]) % 2 == 0:
                    ans = True
                    break
 
            if ans:
                print(2)
            else:
                print(1)
        
        else:
            lst = list(str(k))
            ans = False
            for c in range(0, n, 2):
                if int(lst[c]) % 2 != 0:
                    ans = True
                    break
 
            if ans:
                print(1)
            else:
                print(2)