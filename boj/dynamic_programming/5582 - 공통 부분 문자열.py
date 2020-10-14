s1 = input()
s2 = input()

len1 = len(s1)+1
len2 = len(s2)+1

lcs = [[0]*len1 for _ in range(len2)]
result = 0

maxs = 0

for j in range(1, len2):
    for i in range(1, len1):
        if s1[i-1] == s2[j-1]:
            lcs[j][i] = lcs[j-1][i-1] + 1
            maxs = max(maxs, lcs[j][i])

print(maxs)