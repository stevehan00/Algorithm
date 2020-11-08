n=int(input())
l=[]
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
t=n-1
d=[0 for _ in range(n+1)]
while t>=0:
    if l[t][0]+t<=n: d[t]=max(d[t+1],l[t][1]+d[l[t][0]+t])
    else: d[t]=d[t+1]
    t-=1
print(d[0])