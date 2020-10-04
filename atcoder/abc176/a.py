n,x,t = map(int, input().split())
nums = n//x if n%x is 0 else n//x + 1
print(t*nums)