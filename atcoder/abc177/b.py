s = input()
t = input()
 
maxi = 0
 
for i in range(0, len(s)-len(t)+1):
    temp = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            temp += 1
    maxi = max(temp, maxi)
 
print(len(t) - maxi)