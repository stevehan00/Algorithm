n=int(input())
l=list({0 if((i%3==0) or (i%5==0)) else i for i in range(1,15)}-{0})
print(((n-1)//8)*15+l[n%8-1])