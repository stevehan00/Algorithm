k=int(input())
rm=7%k
an=-1
for i in range(10**6):
	if rm==0:
		an=i+1;break
	rm=(rm*10+7)%k
print(an)