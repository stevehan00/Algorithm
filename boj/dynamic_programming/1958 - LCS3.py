s1 = input()
s2 = input()
s3 = input()

len1 = len(s1)+1
len2 = len(s2)+1
len3 = len(s3)+1

lcs = [[[0 for _ in range(len1)] for _ in range(len2)] for _ in range(len3)]

maxs = 0

for i in range(1, len3):
    for j in range(1, len2):
        for k in range(1, len1):
            if s3[i-1] == s2[j-1] == s1[k-1]:
                lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
            else:
                lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])
            
            maxs = max(maxs, lcs[i][j][k])

print(maxs)