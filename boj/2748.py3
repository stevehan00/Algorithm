n = int(input())

def fibo(num):
    a,b = 1,0
    for i in range(num):
        a,b = b,a+b
    return b

print(fibo(n))