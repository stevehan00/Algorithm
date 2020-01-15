k = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
cnt = 0

for i in range(len(k)):
    s = s.replace(k[i], '0')

print(len(s))